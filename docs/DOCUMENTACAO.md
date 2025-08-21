# Servidor TCP Simples - Documentação

## O que é

Este servidor TCP básico foi desenvolvido em Python puro, sem dependências externas, com o objetivo de aprender o funcionamento de sockets de forma simples. A ideia é entender os conceitos de rede e comunicação, sem a complexidade de frameworks ou bibliotecas extras.

### Arquivos do projeto

- `servidor.py` - Implementação do servidor TCP
- `cliente.py` - Cliente para testar o servidor
- `teste_simples.py` - Teste automatizado

## Por que escolhi essa abordagem

### Simplicidade
A proposta era criar algo direto e fácil de entender. Não queria me perder em complexidade.

### Sem dependências
Eu queria que fosse o mais "puro" possível, sem a necessidade de pacotes externos. O Python já tem tudo o que precisamos com a biblioteca `socket`.

### Didático
O foco aqui é no aprendizado. Todo o código foi feito para ser claro e mostrar os conceitos fundamentais.

### Controle total
Eu preferi fazer cada passo do processo para ver exatamente como ele funciona, o que me deu mais controle sobre o que está acontecendo em cada etapa.

## Decisões Técnicas

### TCP
Escolhi o TCP por ser mais confiável. Ele garante que as mensagens cheguem na ordem certa e sem perdas.

### Porta 12345
Foi uma escolha simples para evitar conflitos com portas mais comuns.

### Buffer de 1024 bytes
1024 bytes é um tamanho padrão e geralmente suficiente para a maioria dos testes.

### UTF-8
O uso de UTF-8 foi essencial para garantir que caracteres especiais e acentos fossem bem tratados.

### Uma conexão por vez
Mantive o servidor simples, aceitando apenas uma conexão por vez, o que facilita o entendimento de como funciona o fluxo de comunicação.

## Como Testar

### Pré-requisitos

- Python instalado (qualquer versão >= 3.x)
- Dois terminais abertos
- A porta 12345 precisa estar livre

### Passos para Testar

#### Terminal 1 - Rodar o Servidor
No primeiro terminal, execute o comando:

```bash
python servidor.py
```

#### Terminal 2 - Rodar o Cliente
No segundo terminal, execute o comando:

```bash
python cliente.py
```

### Fluxo de Teste

1. O servidor inicia no Terminal 1 e começa a escutar por conexões
2. O cliente, ao ser executado no Terminal 2, se conecta ao servidor, envia uma mensagem e recebe a resposta

### Mensagens de Exemplo

Aqui estão algumas mensagens que você pode testar:

- `Olá mundo!`
- `Olá! Como vai você?`
- `Esta é uma mensagem longa...`
- `123456789`
- `!@#$%^&*()`

### Testes de Erro

Você pode também testar alguns cenários para ver como o servidor se comporta:

- **Porta ocupada**: Tente rodar o servidor duas vezes em terminais diferentes para ver o que acontece
- **Cliente sem servidor**: Tente rodar o cliente sem ter o servidor rodando
- **Múltiplas conexões**: Execute o cliente várias vezes e veja o que acontece (lembre-se que o servidor só aceita uma conexão por vez)

## Raciocínio Durante o Desenvolvimento

### Fase 1: Conceituação
Meu objetivo inicial era entender como os sockets funcionam, então pensei: "Vamos fazer algo simples e direto para aprender de fato o que está acontecendo, sem depender de frameworks complexos."

### Fase 2: Estrutura Básica
Comecei com o essencial: criar um socket, ligar (bind), escutar (listen), aceitar conexões (accept), e, claro, receber e enviar mensagens. O código deveria ser o mais simples possível, mas ainda assim funcional.

### Fase 3: Tratamento de Erros
Depois de ver o código funcionando, percebi que ele precisava de mais robustez. Então, adicionei alguns tratamentos de erro, como garantir que a porta não estivesse ocupada e lidar com exceções caso o cliente não consiga se conectar.

### Fase 4: Melhorias
Para facilitar os testes, criei um cliente Python e também uma ferramenta de teste (`teste_simples.py`). Assim ficou bem mais fácil validar a comunicação entre servidor e cliente.

### Fase 5: Reflexão
Apesar de ser uma implementação simples, deu para perceber as limitações do modelo, como o fato de aceitar apenas uma conexão por vez. Mas isso foi intencional, já que o foco era realmente entender o básico do TCP.

## Bibliotecas Utilizadas

### Biblioteca Principal
Somente a biblioteca `socket` (que já vem com o Python)

**Por que essa escolha?** A biblioteca socket oferece o controle total sobre a comunicação de rede sem a necessidade de instalar nada além do Python.

### Alternativas Consideradas

- **asyncio**: Poderia ser uma escolha mais moderna, mas para esse exemplo achei que a abordagem síncrona era mais clara
- **requests**: Embora útil para HTTP, ela abstrai demais e não seria ideal para aprender o protocolo TCP de baixo nível

## Limitações

### Uma conexão por vez
Essa foi uma limitação intencional, para manter o servidor simples e didático. Não dá para lidar com múltiplos clientes simultaneamente.

### Porta fixa
No código, a porta está definida de forma fixa. Isso limita um pouco a flexibilidade, mas mantém a simplicidade.

### Logging básico
O servidor tem um sistema de logs bem simples, só para mostrar as mensagens recebidas. Para um sistema mais robusto, seria necessário um sistema de logs mais detalhado.