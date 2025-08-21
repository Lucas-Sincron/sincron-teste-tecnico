import socket

def start_server():
    # Criação do socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Definir o IP e a porta do servidor
        host = '127.0.0.1'  # IP local
        port = 12345  # Escolha uma porta não utilizada

        # Bind o socket ao endereço
        try:
            server_socket.bind((host, port))
        except OSError as e:
            if e.winerror == 10048:  # Porta já em uso
                print(f"Erro: Porta {port} já está em uso!")
                print("Tente usar outra porta ou aguarde alguns segundos.")
                return
            else:
                raise e

        # Escutar por conexões
        server_socket.listen()

        print(f"Servidor rodando em {host}:{port}")

        # Aceitar a conexão
        conn, addr = server_socket.accept()
        print(f"Conectado a {addr}")

        try:
            # Receber e responder a mensagem
            data = conn.recv(1024)
            if data:  # Verifica se recebeu dados
                print(f"Mensagem recebida: {data.decode('utf-8', errors='ignore')}")
                
                # Enviar confirmação de volta
                conn.sendall(b'Mensagem recebida com sucesso!')
            else:
                print("Cliente desconectou sem enviar dados")
                
        except Exception as e:
            print(f"Erro na comunicação: {e}")
        finally:
            conn.close()
            
    except Exception as e:
        print(f"Erro no servidor: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()