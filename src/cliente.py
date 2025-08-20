import socket

def cliente():
    # Criar socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar ao servidor
        host = '127.0.0.1'
        port = 12345
        
        print(f"Conectando ao servidor {host}:{port}...")
        client_socket.connect((host, port))
        print("Conectado com sucesso!")
        
        # Enviar mensagem
        mensagem = input("Digite sua mensagem: ")
        client_socket.sendall(mensagem.encode('utf-8'))
        
        # Receber resposta
        resposta = client_socket.recv(1024)
        print(f"Resposta do servidor: {resposta.decode()}")
        
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    cliente()