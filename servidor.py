
from os import sys
import sqlite3
import socket
import datetime as dt
#import postgresql
#import mysql.connector as mysql

import socket
import threading
from typing import Text

#import postgresql
#import mysql.connector as mysql

#conexao = postgresql.open('localhost/gpbank')

#conect = mysql.connect(host = 'localhost', db='database', user='usuario', passwd= 'senha')
#conexao = conect.cursor()


class ClientThread(threading.Thread):
    
    def __init__(self, clientAddres, clientsocket,conect, conexao, sinc):
        threading.Thread.__init__(self)
        self.cliente = clientsocket
        self.con = clientAddres
        self.conect = conect
        self.conexao = conexao
        self.sinc = sinc
        print("Nova conexão: ", clientAddres)

    def run(self):
        print("Conectado de: ", self.cliente)
        
        recebe = ''

        while (True):
            recebe = self.con.recv(1024).decode() #define os pacotes recebidos são de ate 1024 bytes 
            variaveis = recebe.split(',')

            
            #conect = sqlite3.connect("gpbank.sqlite")
            #conexao = conect.cursor()
            if(variaveis[0] == 'cad'):
                create = """CREATE TABLE IF NOT EXISTS contas(cpf INTEGER PRIMARY KEY, nome TEXT NOT NULL, sobrenome TEXT NOT NULL, numero INTEGER NOT NULL, limite FLOAT NOT NULL, senha VARCHAR(30) NOT NULL, saldo FLOAT NOT NULL, historico VARCHAR(1000));"""
                self.conexao.execute(create)
                nome = variaveis[1]
                sobrenome = variaveis[2]
                cpf = variaveis[3]
                numero = variaveis[4]
                limite = variaveis[5]
                senha = variaveis[6]
                saldo = 100.0
                historico = "Abertura da conta no dia "+str(dt.datetime.today())
                if(nome == '' or sobrenome == '' or cpf == '', numero == '' or limite == '' or senha == ''):
                    
                    self.conexao.execute("SELECT * FROM contas WHERE cpf ="+cpf)
                    c=None
                    for c in self.conexao:
                        c = c
                    if(c == None):

                        self.sinc.acquire()
                        self.conexao.execute('INSERT INTO contas(cpf, nome, sobrenome, numero, limite, senha, saldo, historico) VALUES (?,?,?,?,?,?,?,?)', (cpf,nome,sobrenome,numero,limite,senha,saldo, historico))
                        self.sinc.release()
                
                        enviar = 'true'
                        #print(conexao.execute('SELECT * FROM contas WHERE cpf='+cpf+' AND senha ='+senha))
                    else:
                        enviar = 'false'
                else:
                    enviar = 'false1'
                self.con.send(enviar.encode())

            elif(variaveis[0] == 'login'):
                login = variaveis[1]
                senha = variaveis[2]
                if not(login == '' or senha == ''):
                    acesso=None
                    self.conexao.execute('SELECT * FROM contas WHERE cpf='+login+' AND senha ='+senha)
                    for a in conexao:
                        acesso = a
                    if (acesso != None):
                        enviar = str(acesso[6])
                        #print(acesso[0])
                    else:
                        enviar="none"
                else:
                    enviar = 'false'
                
                self.con.send(enviar.encode())

            elif(variaveis[0] == 'deposito'):
                valor = variaveis[1]
                cpf = variaveis[2]
                if not(valor == ''):
                    
                    self.conexao.execute("SELECT * FROM contas WHERE cpf="+cpf)

                    conta = None
                    for a in conexao:
                        conta = a
                    if (conta != None):
                        if(float(valor) > 0):
                            new_saldo = float(valor) + conta[6]

                            self.sinc.acquire()
                            self.conexao.execute("UPDATE contas SET saldo="+str(new_saldo)+" WHERE cpf="+cpf)
                            h = conta[7]+";Deposito de "+valor+"R$ em "+str(dt.datetime.today())
                            self.sinc.release()

                            self.sinc.acquire()
                            self.conexao.execute("""
                                            UPDATE contas 
                                            SET historico = ?
                                            WHERE cpf = ? 
                                            """,(h,cpf))
                            self.sinc.release()
                            enviar = 'true,'+str(new_saldo)
                        else:
                            enviar = 'false'
                    else:
                        enviar = 'false1'
                else:
                    enviar = 'false2'
                self.con.send(enviar.encode())

            elif(variaveis[0] == 'saque'):
                cpf = variaveis[1]
                valor = variaveis[2]

                if(valor != ''):
                    sql = "SELECT * FROM contas WHERE cpf="+cpf
                    self.conexao.execute(sql)

                    conta = None

                    for a in conexao:
                        conta = a
                    
                    if(conta != None):
                        if(float(valor) > 0 and float(valor) <= conta[6]):
                            new_saldo = conta[6] - float(valor)

                            update_saldo = "UPDATE contas SET saldo="+str(new_saldo)+' WHERE cpf='+cpf
                            
                            self.sinc.acquire()
                            self.conexao.execute(update_saldo)
                            self.sinc.release()

                            h = conta[7]+';Saque de '+valor+'R$ em '+str(dt.datetime.today())
                            
                            self.sinc.acquire()
                            self.conexao.execute("""
                                            UPDATE contas 
                                            SET historico = ?
                                            WHERE cpf = ? 
                                            """,(h,cpf))
                            self.sinc.release()

                            enviar = 'true,'+str(new_saldo)
                        else:
                            enviar = 'false'
                    else:
                        enviar = 'false1'
                else:
                    enviar = 'false2'
                self.con.send(enviar.encode())

            elif(variaveis[0] == 'transfere'):
                cpf = variaveis[1]
                valor = variaveis[2]
                destino = variaveis[3]
                
                sql  =  "SELECT * FROM contas WHERE numero="+destino
                self.conexao.execute(sql)

                conta_dest = None
                for a in conexao:
                    conta_dest = a

                if(valor != '' and conta_dest != None):
                    sql = "SELECT * FROM contas WHERE cpf="+cpf
                    self.conexao.execute(sql)

                    conta = None

                    for a in conexao:
                        conta = a
                    
                    if(conta != None and conta[6] > float(valor)):
                        
                        new_saldo = conta[6] - float(valor)
                        update_saldo = "UPDATE contas SET saldo="+str(new_saldo)+' WHERE cpf='+cpf

                        self.sinc.acquire()
                        self.conexao.execute(update_saldo)
                        self.sinc.release()
                        new_saldo1 = conta_dest[6] + float(valor)
                        update_saldo1 = "UPDATE contas SET saldo="+str(new_saldo1)+' WHERE numero='+destino
                        self.sinc.acquire()
                        self.conexao.execute(update_saldo1)
                        self.sinc.release()
                        h = conta[7]+';Transferencia de '+str(valor)+'R$ para '+str(conta_dest[3])+' em '+str(dt.datetime.today())
                        
                        self.sinc.acquire()
                        self.conexao.execute("""
                                            UPDATE contas 
                                            SET historico = ?
                                            WHERE cpf = ? 
                                            """,(h,cpf))
                        self.sinc.release()
                        h1 = conta_dest[7]+';Transferencia de '+str(valor)+'R$ recebida da conta '+str(conta[3])+' em '+str(dt.datetime.today())

                        self.sinc.acquire()
                        self.conexao.execute("""
                                            UPDATE contas 
                                            SET historico = ?
                                            WHERE cpf = ? 
                                            """,(h1,conta_dest[0]))
                        self.sinc.release()
                        enviar = 'true,'+str(new_saldo)

                    else:
                        enviar = 'false'
                else:
                    enviar = 'false1'

                self.con.send(enviar.encode())

            elif(variaveis[0] == 'history'):
                cpf = variaveis[1]

                
                sql = "SELECT historico FROM contas WHERE cpf="+cpf
                self.conexao.execute(sql) 
                enviar = ''
                
                for i in conexao:
                    enviar = enviar+i[0]

                self.con.send(enviar.encode())

            self.conect.commit()

            print("from client", recebe)
            if recebe == '/quit':
                break
        print("Cliente at ", self.con, " disconnected")
        
        



if __name__ == '__main__':
    

    host = 'localhost'
    port = 8000
    addr = (host,port)
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  #reinicializa o socket
    serv.bind(addr) #define a porta e quais ips podem se conectar ao servidor
    
    print("servidor iniciado!")
    #con, cliente = serv_socket.accept() #server aguardando conexão
    print("Aguardando conexão...")
    #print("aguardando mensagem")
    enviar = ''

    conect = sqlite3.connect("gpbank.sqlite", check_same_thread=False)
    conexao = conect.cursor()
    
    sinc = threading.Lock()
    while(True):

        serv.listen(1)
        con, cliente = serv.accept()
        #print("Conectado")
        newthread = ClientThread(con, cliente, conect, conexao, sinc)
        newthread.start()
        #newthread.join()
        ##serv.close()
    
    