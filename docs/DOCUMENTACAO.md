# Mini-Servidor - Documentação

## Por que o servidor foi desenvolvido daquela forma?
O código foi criado com foco de ser simples e direto. Foi criado um mini-servidor sem a necessidade de instalar dependências complexas ou configurar um ambiente de desenvolvimento. O uso do protocolo HTTP e do módulo padrão `http.server` se encaixam perfeitamente nesse objetivo, pois são amplamente documentados e fáceis de entender.

## Principais decisões técnicas e trade-offs
-   **Escolha do Protocolo (HTTP):** O HTTP é ideal para este projeto. É um protocolo de comunicação "request-response" simples, que permite demonstrar o conceito de um servidor de forma clara. O trade-off é que, embora seja perfeito para um mini-servidor, ele não seria a escolha ideal para aplicações que exigem comunicação bidirecional em tempo real, como websockets.

## O que passou pela sua cabeça durante o desenvolvimento (raciocínio)?
Meu raciocínio se baseou em fazer algo simples. Levando em consideração o objetivo: um servidor simples e local. Então decidi usar o módulo `http.server`. Ele é perfeito para o caso, pois já lida com a parte de rede (sockets) e o parsing básico do HTTP, permitindo focar apenas na lógica da resposta (`do_GET`). 

## Como testar manualmente?
Você pode testar o servidor manualmente ao rodar o script e utilizar o navegador da web. Abra o seu navegador preferido e digite a URL `http://localhost:8000` na barra de endereço. Você deve ver a mensagem "Metal Gear Solid" na página.


## Justificativa de bibliotecas externas
Não foram utilizadas bibliotecas externas neste projeto. A solução foi inteiramente baseada na **biblioteca padrão do Python (`http.server` e `socketserver`)**. Essa decisão foi tomada intencionalmente para tornar o servidor **auto-suficiente** e **facilmente executável** sem qualquer etapa de instalação de dependências, assim realizando o objetivo de fazer um servidor local.