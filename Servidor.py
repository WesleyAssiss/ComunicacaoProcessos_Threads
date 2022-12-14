import socket
import threading


def cria_clientes(cliente, endereco):
    """
    Recebe e envia mensagem para cliente
    :param cliente:
    :param endereco:
    :return: null
    """
    while True:
        print("Conexao aceita de: ", endereco)
        mensagem = cliente.recv(2048)
        print("Mensagem recebida: ", mensagem.decode())

        mensagem = "Ola o que posso ajudar?:"
        cliente.send(mensagem.encode())


def server():
    """
    Cria Threads para receber conexões de vários clientes.
    :return: null
    """
    while True:
        cliente, endereco = servidor.accept()
        threading.Thread(target=cria_clientes, args=(cliente,endereco)).start()
       

if __name__ == '__main__':
    PORTA = 14500
    servidor = socket.socket()
    servidor.bind(("localhost", PORTA))
    servidor.listen(5)
    print("Servidor escutando na porta: ", PORTA)
    threading.Thread(target=server, args=()).start()
