import socket

ip = "localhost"
port = 8000
addr = ((ip,port)) ##tupla  de endereço

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que é TCP/IP
cliente_socket.connect(addr) #conexão

while(True):
    mensagem = input("Digite uma mensagem para enviar ao servidor: ")
    if(mensagem == '/quit'):
        break
    cliente_socket.send(mensagem.encode()) #send message
    #print("Mensagem enviada")
    recebe = cliente_socket.recv(1024).decode()
    if(recebe != '/quit'):
        print("mensagem recebida:" + recebe)
    else:
        break

cliente_socket.send('/quit'.encode())
cliente_socket.close() #fecha conexão