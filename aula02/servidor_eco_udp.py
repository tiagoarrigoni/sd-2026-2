import socket


HOST, PORT = "127.0.0.1", 5000               # localhost + porta escolhida


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reusar a porta
s.bind((HOST, PORT))                          # reserva o endereço
print(f"[servidor] ouvindo em {HOST}:{PORT}", flush=True)


while True:
    dado, endereco = s.recvfrom(1024)         # RECEBE bytes e endereço do cliente

    print(f"[servidor] cliente conectado: {endereco}", flush=True)
    print(f"[servidor] recebi: {dado.decode()}", flush=True)

    s.sendto(dado, endereco)                   # ECO: devolve o mesmo

s.close()