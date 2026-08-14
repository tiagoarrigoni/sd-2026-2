import socket


HOST, PORT = "127.0.0.1", 5000


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
print("Conectado. Digite mensagens (ou 'sair'):")

while True:
    msg = input("> ")
    if msg == "sair":
        break

    s.sendto(msg.encode(), (HOST, PORT))               # ENVIA bytes
    eco, endereco = s.recvfrom(1024)                   # RECEBE o eco
    print("eco:", eco.decode())

s.close()