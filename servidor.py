import sys
import socket
import os
import mysql.connector as mysql

conexao = mysql.connect(host = 'lacalhost', db='gpbank', user='root', passwd = '')
cursor = conexao.cursor()

host = 'localhost'
port = 8000
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket
serv_socket.bind(addr) #define a porta e quais ips podem se conectar ao servidor
serv_socket.listen(10) #define o limite de conexões
print("aguardando conexão...")
con, cliente = serv_socket.accept() #server aguardando conexão
print("conectado")
print("aguardando mensagem")
enviar = ''

while(enviar != 'sair'):
    recebe = con.recv(1024).decode() #define os pacotes recebidos são de ate 1024 bytes 
    variaveis = recebe.split(',')
    if(variaveis[0] == 'cad'):
        create = """CREATE TABLE IF NOT EXISTS contas(cpf INTEGER PRIMARY KEY, nome TEXT NOT NULL, sobrenome TEXT NOT NULL, numero INTEGER NOT NULL, limite FLOAT NOT NULL, senha VARCHAR(30) NOT NULL, saldo FLOAT NOT NULL);"""
        cursor.execute(create)
        nome = variaveis[1]
        sobrenome = variaveis[2]
        cpf = variaveis[3]
        numero = variaveis[4]
        limite = variaveis[5]
        senha = variaveis[6]
        saldo = 0.0
        if(nome == '' or sobrenome == '' or cpf == '', numero == '' or limite == '' or senha == ''):
            sql = "SELECT * FROM contas WHERE cpf = "+cpf+','
            cursor.execute(sql)
            c=None
            for c in cursor:
               c = c
            if(c == None):
                add = 'INSERT INTO contas(cpf, nome, sobrenome, numero, limite, senha, saldo) VALUES ('+cpf+',"'+nome+'", "'+sobrenome+'", '+numero+', '+limite+', "'+senha+'", '+saldo+');'
                cursor.execute(add)
                enviar = 'true'
            else:
                enviar = 'false'

            con.send(enviar.encode())

        elif(variaveis[0] == 'login'):
            login = variaveis[1]
            senha = variaveis[2]
            if not(login == '' or senha == ''):
                sql = 'SELECT * FROM contas WHERE cpf="'+cpf+'" AND senha="'+senha+'");'
                acesso=None
                cursor.execute(sql)
                for acesso in cursor:
                    acesso = acesso
                if (acesso != None):
                    enviar = str(acesso[0])
                else:
                    enviar="none"
            else:
                enviar = 'false'
            
            con.send(enviar.encode())

        elif(variaveis[0] == 'deposito'):
            valor = variaveis[1]
            cpf = variaveis[2]
            if not(valor == '' or cpf == ''):
                
                sql = "SELECT * FROM contas WHERE cpf="+cpf
                cursor.execute(sql)

                conta = None
                for a in cursor:
                    conta = a
                if (conta != None):
                    if(float(valor) > 0):
                        new_saldo = float(valor) + conta[6]

                        create1= """CREATE TABLE IF NOT EXISTS historico(cpf INTEGER PRIMARY KEY, 
                        valor FLOAT NOT NULL, tipo_operacao TEXT NOT NULL, cpf_destino INTEGER);"""

                        cursor.execute(create1)

                        update_saldo = "UPDATE contas SET saldo="+new_saldo+' WHERE cpf='+cpf
                        cursor.execute(update_saldo)

                        registra = "INSERT INTO historico (cpf, valor, tipo_operacao, cpf_destino) VALUES ("+conta[1]+float(valor)+"'Deposito'"+conta[1]+")"

                        cursor.execute(registra)

                        enviar = 'true,'+new_saldo
                    else:
                        enviar = 'false,NaN'
                else:
                    enviar = 'false1,NaN'
            else:
                enviar = 'false2,NaN'
            con.send(enviar.encode())

        elif(variaveis[0] == 'saque'):
            pass
        elif(variaveis[0] == 'transfere'):
            pass
        elif(variaveis[0] == 'history'):
            cpf = variaveis[1]

            sql = "SELECT * FROM contas WHERE cpf="+cpf
            cursor.execute(sql) 

            conta = None
            for i in cursor:
                conta = i
            if(conta != None):
                sql = "SELECT * FROM historico WHERE cpf="+cpf
                cursor.execute(sql) 
                enviar = ''

                enviar+conta[1]+','+conta[0]+','+conta[6]
                for i in cursor:
                    if(i[2] == 'Deposito' or i[2] == 'Saque'):
                        enviar+','+i[2]+','+'de,'+i[1]
                    else:
                        enviar+','+i[2]+','+'de,'+i[1]+'para,'+i[3]
            else:
                enviar = 'false'
           
            con.send(enviar.encode())
                    
        else:
            enviar = 'sair'
            con.send(enviar.encode())

serv_socket.close()