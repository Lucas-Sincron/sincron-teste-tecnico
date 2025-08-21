# Documentação do Mini Servidor

## Motivação
Escolhi criar um **servidor TCP simples** para demonstrar comunicação básica entre cliente e servidor e facilitar o teste local. A ideia era mostrar que consigo receber mensagens, processá-las e devolver respostas de forma clara, mesmo com um código pequeno.

---

## Decisões técnicas
- **Python puro:** não usei frameworks ou bibliotecas externas para manter o servidor simples e fácil de rodar em qualquer máquina.  
- **JSON como formato de mensagens:** é legível, padrão e fácil de trabalhar.  
- **TCP:** escolhi esse protocolo por ser confiável, garante que as mensagens chegam ao destino sem perda.

---

## Trade-offs (decisões que fiz e alternativas)
- Usei **um servidor simples com loop e fechamento da conexão a cada mensagem**.  
  - **Vantagem:** código fácil de entender, bom para aprendizado e teste rápido.  
  - **Desvantagem:** não suporta múltiplos clientes ao mesmo tempo de forma eficiente. Em projetos maiores, seria melhor usar **threads** ou **asyncio**.  
- Mantive apenas **comandos básicos (`ping` e `hora`)**.  
  - **Vantagem:** atende aos requisitos do teste e permite testar rapidamente.  
  - **Desvantagem:** servidor ainda não é “completo” ou genérico, mas para este teste é suficiente.

> Em resumo, escolhi **simplicidade e clareza** em vez de complexidade ou recursos avançados. Isso ajuda a focar no objetivo do teste sem criar problemas desnecessários.

---

## Raciocínio
Comecei pensando em **como receber mensagens e responder de forma imediata**, usando JSON.  
Depois criei comandos simples para testar comunicação (`ping` e `hora`) e garantir que o servidor funcionaria em um ambiente local.

---

## Teste manual
1. Abrir o terminal na pasta do projeto e rodar o servidor:

```bash
python src/server.py

---
2. Abrir outro terminal (ou aba) para testar com Python:

Comando ping ⬇
---

import socket, json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65432))
client.sendall(json.dumps({"command": "ping"}).encode())
data = client.recv(1024)
print("Resposta do servidor:", data.decode())
client.close()

---
Comando hora ⬇


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65432))
client.sendall(json.dumps({"command": "hora"}).encode())
data = client.recv(1024)
print("Resposta do servidor:", data.decode())
client.close()
---
Se aparecer {"response": "pong"} ou a hora atual, o servidor está funcionando corretamente.