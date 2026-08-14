import socket
import threading


HOST, PORT = "127.0.0.1", 5000


contador_clientes = 0
lock = threading.Lock()


def atender_cliente(conexao, endereco, codigo_cliente):
    print(
        f"[servidor] {codigo_cliente} conectado: {endereco}",
        flush=True
    )

    while True:
        dado = conexao.recv(1024)

        if not dado:
            break

        print(
            f"[{codigo_cliente}] recebi: {dado.decode()}",
            flush=True
        )

        conexao.sendall(dado)

    conexao.close()

    print(
        f"[servidor] {codigo_cliente} desconectou.",
        flush=True
    )


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

s.bind((HOST, PORT))
s.listen()

print(
    f"[servidor] ouvindo em {HOST}:{PORT}",
    flush=True
)


while True:
    conexao, endereco = s.accept()

    with lock:
        contador_clientes += 1
        codigo_cliente = f"Cliente {contador_clientes}"

    threading.Thread(
        target=atender_cliente,
        args=(conexao, endereco, codigo_cliente)
    ).start()