import socket

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


while(True):
    recebe = con.recv(1024).decode() #define os pacotes recebidos são de ate 1024 bytes
    print("mensagem recebida: " + recebe)
    if(recebe != '/quit'):
        enviar = input("Digite uma mensagem para enviar ao cliente: ")
        con.send(enviar.encode())
        if(enviar == '/quit'):
            break
    else:
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("aguardando conexão...")
        con, cliente = serv_socket.accept() #server aguardando conexão
        print("conectado")
        print("aguardando mensagem")

con.send('/quit'.encode())
serv_socket.close()