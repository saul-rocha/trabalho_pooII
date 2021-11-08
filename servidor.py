<<<<<<< HEAD
import sqlite3
import socket
import datetime as dt
#import postgresql
#import mysql.connector as mysql
=======
import socket

#import postgresql
import mysql.connector as mysql
>>>>>>> 89beed39761668d2a5efeeaa2ce66cffd49be626


#conexao = postgresql.open('localhost/gpbank')

conect = mysql.connect(host = 'localhost', db='database', user='usuario', passwd= 'senha')
conexao = conect.cursor()

conect = sqlite3.connect("gpbank.sqlite")
conexao = conect.cursor()

host = 'localhost'
port = 8000
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
serv_socket.setsockopt  #reinicializa o socket
serv_socket.bind(addr) #define a porta e quais ips podem se conectar ao servidor
serv_socket.listen(10) #define o limite de conexões
print("aguardando conexão...")
con, cliente = serv_socket.accept() #server aguardando conexão
print("conectado")
print("aguardando mensagem")
enviar = ''

while(enviar != 'sair'):
    conect = sqlite3.connect("gpbank.sqlite")
    conexao = conect.cursor()
    recebe = con.recv(1024).decode() #define os pacotes recebidos são de ate 1024 bytes 
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
<<<<<<< HEAD
                
                conexao.execute('INSERT INTO contas(cpf, nome, sobrenome, numero, limite, senha, saldo, historico) VALUES (?,?,?,?,?,?,?,?)', (cpf,nome,sobrenome,numero,limite,senha,saldo, historico))
=======
                add = 'INSERT INTO contas(cpf, nome, sobrenome, numero, limite, senha, saldo) VALUES ('+cpf+',"'+nome+'", "'+sobrenome+'", '+numero+', '+limite+', "MD5('+senha+')", '+saldo+');'
                conexao.execute(add)
>>>>>>> 89beed39761668d2a5efeeaa2ce66cffd49be626
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
<<<<<<< HEAD
=======
            sql = 'SELECT * FROM contas WHERE cpf="'+cpf+'" AND senha="MD5('+senha+')";'
>>>>>>> 89beed39761668d2a5efeeaa2ce66cffd49be626
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

    con.send(enviar.encode())
    enviar = ''

conect.close()
serv_socket.close()