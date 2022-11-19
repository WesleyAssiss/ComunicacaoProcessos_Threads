import socket


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 15000))
mensagem = "Olá: "

while mensagem != 'x':



    mensagem = input("Digite uma mensagem: ")
    cliente.send(mensagem.encode())

    recebido = cliente.recv(2048)
    print("Mensagem recebida: ", str(recebido.decode()))
cliente.close()

    #mensagem = cliente.recv(1024)
    #print("Mensagem recebida: ", mensagem.decode())
    #cliente.close()