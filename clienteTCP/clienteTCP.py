import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socekt.error as e:
        print("A Conexão falhou!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    hostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((hostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + hostAlvo +" e na Porta "+ PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host: " + hostAlvo + "- Porta " + PortaAlvo)
        print("Erro : {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()

