# Documentação do Servidor

## Introdução
Este servidor foi implementado em Python utilizando o módulo `socket` para criar uma comunicação TCP. O servidor escuta na porta 65432 e aguarda conexões de clientes. Quando uma conexão é estabelecida, ele envia uma resposta simples.

## Como o servidor funciona
1. O servidor é inicializado com o IP `127.0.0.1` (localhost) e escuta na porta `65432`.
2. Quando um cliente se conecta, a conexão é aceita e uma mensagem de "Conexão estabelecida" é exibida no terminal do servidor.
3. Após a conexão ser estabelecida, o servidor espera por dados do cliente. Quando os dados são recebidos, o servidor os envia de volta ao cliente (simples echo).

## Decisões Tomadas
1. **Escolha do Protocolo**: Utilizei o protocolo TCP para garantir uma comunicação confiável entre o servidor e o cliente, onde a ordem dos pacotes e a entrega são importantes.
2. **Escolha do Python**: Python foi escolhido por ser uma linguagem de fácil entendimento e por já possuir a biblioteca `socket` integrada, facilitando a implementação.
3. **Segurança**: O servidor está operando no localhost, o que significa que ele só pode ser acessado pela máquina local para fins de teste e desenvolvimento.

## Conclusão
Este servidor simples é um exemplo de como implementar um sistema de comunicação em rede utilizando o protocolo TCP. Ele pode ser expandido para incluir mais funcionalidades, como autenticação de usuários, encriptação de dados, etc.
