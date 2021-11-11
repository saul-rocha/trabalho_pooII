
from os import SEEK_CUR
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
    
    def __init__(self, clientAddres, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexão: ", clientAddres)

    def run(self):
        print("Conectado de: ", clientAddres)
        mensagem = ''

        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            self.csocket.send(msg.encode())
            print("from client", msg)
            if msg == '/quit':
                break
        print("Cliente at ", clientAddres, " disconnected")




if __name__ == '__main__':
    conect = sqlite3.connect("gpbank.sqlite")
    conexao = conect.cursor()

    localhost = ''
    port = 8000

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  #reinicializa o socket
    serv.bind(localhost,port) #define a porta e quais ips podem se conectar ao servidor
    serv.listen(10) #define o limite de conexões
    print("servidor iniciado!")
    #con, cliente = serv_socket.accept() #server aguardando conexão
    print("Aguardando conexão...")
    #print("aguardando mensagem")
    enviar = ''

    while(True):
        conect = sqlite3.connect("gpbank.sqlite")
        conexao = conect.cursor()
        
        serv.listen(1)
        clientsock, clientAddres = serv.accept()
        newtrhead = ClientThread(clientAddres, clientsock)
        newtrhead.start()
        recebe = clientsock.recv(1024).decode() #define os pacotes recebidos são de ate 1024 bytes 
        variaveis = recebe.split(',')
        if(variaveis[0] == 'cad'):
            create = """CREATE TABLE IF NOT EXISTS contas(cpf INTEGER PRIMARY KEY, nome TEXT NOT NULL, sobrenome TEXT NOT NULL, numero INTEGER NOT NULL, limite FLOAT NOT NULL, senha VARCHAR(30) NOT NULL, saldo FLOAT NOT NULL, historico VARCHAR(1000));"""
            conexao.execute(create)
            nome = variaveis[1]
            sobrenome = variaveis[2]
            cpf = variaveis[3]
            numero = variaveis[4]
            limite = variaveis[5]
            senha = variaveis[6]
            saldo = 100.0
            historico = "Abertura da conta no dia "+str(dt.datetime.today())
            if(nome == '' or sobrenome == '' or cpf == '', numero == '' or limite == '' or senha == ''):
                
                conexao.execute("SELECT * FROM contas WHERE cpf ="+cpf)
                c=None
                for c in conexao:
                    c = c
                if(c == None):

                    
                    conexao.execute('INSERT INTO contas(cpf, nome, sobrenome, numero, limite, senha, saldo, historico) VALUES (?,?,?,?,?,?,?,?)', (cpf,nome,sobrenome,numero,limite,senha,saldo, historico))

            
                    enviar = 'true'
                    #print(conexao.execute('SELECT * FROM contas WHERE cpf='+cpf+' AND senha ='+senha))
                else:
                    enviar = 'false'
            else:
                enviar = 'false1'
                #con.send(enviar.encode())


        elif(variaveis[0] == 'login'):
            login = variaveis[1]
            senha = variaveis[2]
            if not(login == '' or senha == ''):
                acesso=None
                conexao.execute('SELECT * FROM contas WHERE cpf='+login+' AND senha ='+senha)
                for a in conexao:
                    acesso = a
                if (acesso != None):
                    enviar = str(acesso[6])
                    #print(acesso[0])
                else:
                    enviar="none"
            else:
                enviar = 'false'
            
            #con.send(enviar.encode())

        elif(variaveis[0] == 'deposito'):
            valor = variaveis[1]
            cpf = variaveis[2]
            if not(valor == ''):
                
                conexao.execute("SELECT * FROM contas WHERE cpf="+cpf)

                conta = None
                for a in conexao:
                    conta = a
                if (conta != None):
                    if(float(valor) > 0):
                        new_saldo = float(valor) + conta[6]

                        conexao.execute("UPDATE contas SET saldo="+str(new_saldo)+" WHERE cpf="+cpf)
                        h = conta[7]+";Deposito de "+valor+"R$ em "+str(dt.datetime.today())
                        
                        conexao.execute("""
                                        UPDATE contas 
                                        SET historico = ?
                                        WHERE cpf = ? 
                                        """,(h,cpf))

                        enviar = 'true,'+str(new_saldo)
                    else:
                        enviar = 'false'
                else:
                    enviar = 'false1'
            else:
                enviar = 'false2'
            #con.send(enviar.encode())

        elif(variaveis[0] == 'saque'):
            cpf = variaveis[1]
            valor = variaveis[2]

            if(valor != ''):
                sql = "SELECT * FROM contas WHERE cpf="+cpf
                conexao.execute(sql)

                conta = None

                for a in conexao:
                    conta = a
                
                if(conta != None):
                    if(float(valor) > 0 and float(valor) <= conta[6]):
                        new_saldo = conta[6] - float(valor)

                        update_saldo = "UPDATE contas SET saldo="+str(new_saldo)+' WHERE cpf='+cpf
                        conexao.execute(update_saldo)

                        h = conta[7]+';Saque de '+valor+'R$ em '+str(dt.datetime.today())

                        conexao.execute("""
                                        UPDATE contas 
                                        SET historico = ?
                                        WHERE cpf = ? 
                                        """,(h,cpf))
                        
                        enviar = 'true,'+str(new_saldo)
                    else:
                        enviar = 'false'
                else:
                    enviar = 'false1'
            else:
                enviar = 'false2'
            #con.send(enviar.encode())

        elif(variaveis[0] == 'transfere'):
            cpf = variaveis[1]
            valor = variaveis[2]
            destino = variaveis[3]
            
            sql  =  "SELECT * FROM contas WHERE numero="+destino
            conexao.execute(sql)

            conta_dest = None
            for a in conexao:
                conta_dest = a

            if(valor != '' and conta_dest != None):
                sql = "SELECT * FROM contas WHERE cpf="+cpf
                conexao.execute(sql)

                conta = None

                for a in conexao:
                    conta = a
                
                if(conta != None and conta[6] > float(valor)):
                    
                    new_saldo = conta[6] - float(valor)
                    update_saldo = "UPDATE contas SET saldo="+str(new_saldo)+' WHERE cpf='+cpf
                    conexao.execute(update_saldo)

                    new_saldo1 = conta_dest[6] + float(valor)
                    update_saldo1 = "UPDATE contas SET saldo="+str(new_saldo1)+' WHERE numero='+destino
                    conexao.execute(update_saldo1)

                    h = conta[7]+';Transferencia de '+str(valor)+'R$ para '+str(conta_dest[3])+' em '+str(dt.datetime.today())
                    
                    conexao.execute("""
                                        UPDATE contas 
                                        SET historico = ?
                                        WHERE cpf = ? 
                                        """,(h,cpf))
                    h1 = conta_dest[7]+';Transferencia de '+str(valor)+'R$ recebida da conta '+str(conta[3])+' em '+str(dt.datetime.today())

                    conexao.execute("""
                                        UPDATE contas 
                                        SET historico = ?
                                        WHERE cpf = ? 
                                        """,(h1,conta_dest[0]))

                    enviar = 'true,'+str(new_saldo)

                else:
                    enviar = 'false'
            else:
                enviar = 'false1'

            #con.send(enviar.encode())

        elif(variaveis[0] == 'history'):
            cpf = variaveis[1]

            
            sql = "SELECT historico FROM contas WHERE cpf="+cpf
            conexao.execute(sql) 
            enviar = ''
            
            for i in conexao:
                enviar = enviar+i[0]
                
                    

        conect.commit()
        conect.close()

        clientsock.send(enviar.encode())
        enviar = ''

    conect.close()
    serv.close()