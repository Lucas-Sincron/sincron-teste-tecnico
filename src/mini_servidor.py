import socket     #Biblioteca nativa do Python para comunicação via rede
import threading  #Permite executar múltiplas tarefas simultaneamente (multithreading)

class MiniServidor:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        
    def iniciar(self):
        #Inicia o servidor
        try:
            # Cria o socket TCP
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Associa o socket ao host e porta
            self.server_socket.bind((self.host, self.port))
            
            # Começa a escutar por conexões
            self.server_socket.listen(5)
            self.running = True
            
            print(f"Servidor iniciado em {self.host}:{self.port}")
            print("Aguardando conexões...")
            print("Digite 'sair' para encerrar o servidor")
            
            # Thread para monitorar comandos do console
            console_thread = threading.Thread(target=self.monitorar_console)
            console_thread.daemon = True
            console_thread.start()
            
            # Aceita conexões
            while self.running:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    print(f"Nova conexão de {client_address}")
                    
                    # Cria uma thread para lidar com o cliente
                    client_thread = threading.Thread(
                        target=self.lidar_com_cliente, 
                        args=(client_socket, client_address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
                except OSError:
                    break
                    
        except Exception as e:
            print(f"Erro ao iniciar servidor: {e}")
        finally:
            self.encerrar()
    
    def lidar_com_cliente(self, client_socket, client_address):
        #Lida com a comunicação com um cliente específico
        try:
            with client_socket:
                while self.running:
                    # Recebe dados do cliente
                    data = client_socket.recv(1024).decode('utf-8')
                    
                    if not data:
                        break
                    
                    print(f"Mensagem de {client_address}: {data}")
                    
                    # Comando especial para encerrar conexão
                    if data.strip().lower() == 'sair':
                        resposta = "Conexão encerrada. Até logo!"
                        client_socket.send(resposta.encode('utf-8'))
                        break
                    
                    # Resposta padrão (eco da mensagem)
                    resposta = f"Eco: {data}"
                    client_socket.send(resposta.encode('utf-8'))
                    
        except ConnectionResetError:
            print(f"Conexão com {client_address} foi resetada")
        except Exception as e:
            print(f"Erro na conexão com {client_address}: {e}")
        finally:
            print(f"Cliente {client_address} desconectado")
    
    def monitorar_console(self):
        #Monitora comandos do console para controlar o servidor
        while self.running:
            comando = input().strip().lower()
            if comando == 'sair':
                print("Encerrando servidor...")
                self.running = False
                # Fecha o socket para sair do loop de accept()
                if self.server_socket:
                    try:
                        # Cria um socket temporário para forçar o accept() a falhar
                        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        temp_socket.connect((self.host, self.port))
                        temp_socket.close()
                    except:
                        pass
    
    def encerrar(self):
        #Encerra o servidor
        print("Encerrando servidor...")
        if self.server_socket:
            self.server_socket.close()
        print("Servidor encerrado com sucesso")

def main():
    #Função principal
    servidor = MiniServidor()
    
    try:
        servidor.iniciar()
    except KeyboardInterrupt:
        print("\nServidor interrompido pelo usuário")
        servidor.encerrar()

if __name__ == "__main__":
    main()