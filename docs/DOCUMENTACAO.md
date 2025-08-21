1. **Por que o servidor foi desenvolvido daquela forma;**

    - O servidor TCP foi desenvolvido para ser confiável, utilizando sockets que garantem a entrega de dados na ordem correta. A implementação de multithreading permite atender múltiplos clientes simultaneamente, melhorando a responsividade. O código é organizado em uma classe com métodos distintos, facilitando a manutenção e reutilização. O tratamento de exceções aumenta a robustez do servidor, evitando falhas inesperadas e fornecendo feedback ao usuário. A interação com o console permite controle direto do servidor, como encerrar a operação com um comando simples ("sair"). A funcionalidade de eco de mensagens demonstra a comunicação básica entre cliente e servidor. Comentários no código ajudam na compreensão e manutenção. Essas escolhas visam criar um servidor simples, robusto e fácil de usar, servindo como uma base sólida para entender programação de redes.

2. **Principais decisões técnicas e trade-offs;**

    - As principais decisões técnicas no desenvolvimento do servidor TCP incluem a escolha do protocolo TCP, que oferece confiabilidade e entrega ordenada de dados, em contraste com UDP, que é mais rápido, mas não garante essas características. A implementação de multithreading permite que o servidor atenda múltiplos clientes simultaneamente, melhorando a responsividade, mas introduz complexidade na gestão de threads e possíveis condições de corrida. A estrutura modular do código facilita a manutenção e reutilização, mas pode resultar em um aumento no número de arquivos e na complexidade do projeto. O tratamento de exceções é crucial para a robustez do servidor, mas pode tornar o código mais extenso e difícil de seguir. A interação com o console oferece um controle intuitivo, mas limita a escalabilidade e a integração com interfaces gráficas. Por fim, a funcionalidade de eco de mensagens é simples e eficaz para demonstração, mas não oferece funcionalidades avançadas que poderiam ser exploradas em um servidor mais complexo. Essas decisões refletem um equilíbrio entre simplicidade, robustez e funcionalidade, visando criar uma base sólida para aplicações de rede.

3. **O que passou pela sua cabeça durante o desenvolvimento (raciocínio);**

    - Durante o desenvolvimento do servidor TCP, priorizei a simplicidade e a confiabilidade, escolhendo o TCP por sua entrega ordenada de dados. Estruturei o código em uma única classe para facilitar a compreensão e optei por multithreading para atender múltiplos clientes simultaneamente. Implementei context managers para garantir o fechamento adequado de sockets e adicionei controle via console para um encerramento gracioso. O tratamento de erros foi incluído para manter a estabilidade do servidor. O foco foi criar um código claro e didático, servindo como uma base sólida para aplicações de rede.

4. **Como testar manualmente (ex.: exemplos de mensagens/requests);**

    -Você pode testar um servidor TCP manualmente de três formas:

    Telnet: abra o terminal e conecte com telnet localhost <porta>, depois envie mensagens.

    Netcat (nc): use nc localhost <porta> e digite mensagens para o servidor responder.

    Script Python: crie um cliente simples usando socket para enviar e receber mensagens.

    Exemplos de mensagens para teste:

    "Olá, servidor!"

    "Como você está?"

    "Teste de eco."

    "Sair" (se configurado para encerrar).

    Certifique-se de que o servidor esteja rodando, a porta correta esteja liberada, e faça testes também com múltiplas conexões.

5. **Justificativa de bibliotecas externas, se houver.**

    - Utilizei duas:  
    socket: Biblioteca nativa do Python para comunicação via rede;
    threading: Permite executar múltiplas tarefas simultaneamente (multithreading).