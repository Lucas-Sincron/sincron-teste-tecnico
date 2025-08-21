import socket
import json
from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor rodando em {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"Conectado por {addr}")
    data = conn.recv(1024)
    if not data:
        break

    try:
        message = json.loads(data.decode())
        if message.get("command") == "ping":
            response = {"response": "pong"}
        elif message.get("command") == "hora":
            response = {"response": datetime.now().isoformat()}
        else:
            response = {"response": "comando desconhecido"}
    except:
        response = {"response": "erro ao processar mensagem"}

    conn.sendall(json.dumps(response).encode())
    conn.close()
