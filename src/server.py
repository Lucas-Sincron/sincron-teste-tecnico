import socket

# Configuração do servidor
host = '127.0.0.1'  # Endereço local
port = 65432  # Porta do servidor

# Criação do socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor ouvindo na porta {port}...")
    
    # Aguardando a conexão de um cliente
    conn, addr = server_socket.accept()
    with conn:
        print(f"Conexão estabelecida com {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # Enviar de volta os dados recebidos

