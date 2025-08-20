# 📝 Teste de Vaga — Sincron

## 📌 Contexto
Bem-vindo(a)!  
O objetivo deste teste é entender **como você pensa e trabalha**. Se aprovado(a), ira para a proxima parte do processo seletivo.

Serão avaliados:  
- Resultado final  
- Clareza e sinceridade nas respostas  
- Organização do repositório e do código  
- Qualidade do português  
- Boas práticas de desenvolvimento

---

## 🎯 Objetivos do teste
O teste possui duas partes complementares:

1. **Perguntas teóricas** — avaliar conhecimento técnico e raciocínio.  
2. **Desenvolvimento prático** — criação de um **mini servidor** em Python ou NestJS usando um protocolo de comunicação simples (ex.: MQTT, TCP, UDP, Serial, etc.). Além do servidor, é obrigatório entregar uma **mini documentação** que explique as decisões tomadas e o raciocínio por trás do desenvolvimento.

---

## 📝 Parte 1 — Perguntas (responda com clareza e sinceridade)
Responda em linguagem clara e direta. A sinceridade é um critério de avaliação importante.

1. **Conhece os princípios SOLID?**  
   - Se sim: liste-os e descreva aplicações práticas ou exemplos onde já os aplicou.

   R: Não conhecia, porém após umas pesquisas, descobri que SOLID são os cinco princípios da POO(Programação Orientada a Objetos) com qual já trabalhei em Python.
      S - Single Responsibility Principle: Princípio que diz que uma classe deve ter uma única função, um único propósito
      O - Open Closed Principle: Este explica que podemos generalizar classes, com elas abertas para extensão e fechadas para modificação
      L - Liskov Substitution Principle: Pelo meu entendimento se fala muito do conceito de herança em POO, ou seja, uma classe-filha deve herdar todos os aspectos da classe-mãe
      I - Interface Segregation Principle: Devemos criar interfaces específicas ao invés de interfaces genéricas
      D - Dependency Inversion Principle: Dependa de abstrções e não de informações concretas.


2. **Conhece protocolos de comunicação além do HTTP?**  
   - Se sim: cite quais e onde já os utilizou ou poderia utilizar.

   R: Não, só utilizei protocolos HTTP, junto com Python, Javascript e SQL Server em projetos do SENAI.
      Pórem se necessário para vaga estou disposto aprender cada dia mais outros protocolos para contribuir com a empresa.

3. **Conhece dispositivos IoT?**  
   - Se sim: liste dispositivos/plataformas com que já trabalhou (ex.: ESP32, Raspberry Pi, LoRa nodes, sensores, etc.).

   R: Sim, já mexi em dispositivos IoT interligados com Arduino e utilizando Node Red, já trabalhei com sensores e também com um pouco de APIs.


4. **Pretende usar ou usou IA para alguma parte deste teste?**  
   - **Se sim**: informe qual(is) ferramenta(s), em que parte foi usada e por que (seja específico).  
   - **Se não**: explique por que optou por não usar IA.

   R: Neste quase não usei IA, porque quis programar um código mais simples e funcional, desde modo precisei ver mais a documentação e um pequeno vídeo no youtube. O único momento que IA - Gemini - foi necessária foi para entender melhor a organização e a estrtutra das pastas.

---

## 💻 Parte 2 — Desenvolvimento (prático)
Requisitos e expectativas:

- **Escolha um protocolo de comunicação simples** e implemente um **mini servidor** que rode localmente.  
- **Linguagem:** Python **ou** NestJS (sem restrição de versão).  
- O servidor deve ser fácil de executar localmente — inclua instruções claras de execução.  
- **Mini documentação obrigatória** (`docs/DOCUMENTACAO.md`) contendo:
  - Por que o servidor foi desenvolvido daquela forma;
  - Principais decisões técnicas e trade-offs;
  - O que passou pela sua cabeça durante o desenvolvimento (raciocínio);
  - Como testar manualmente (ex.: exemplos de mensagens/requests);
  - Justificativa de bibliotecas externas, se houver.  
- É permitido usar bibliotecas e ferramentas externas — **justifique** cada escolha na documentação.

---

## 📦 Como entregar
1. Faça **fork** deste repositório.  
2. Crie um **branch** com o seu nome no formato:

Ex.: `joao-silva`  
3. Preencha `RESPOSTAS.md` com as respostas teóricas.  
4. Coloque o código do servidor dentro de `src/`.  
5. Escreva a **mini documentação** em `docs/DOCUMENTACAO.md`.  
6. Faça commits limpos e significativos.  
7. Abra um **Pull Request** para este repositório quando terminar.

**Prazo de entrega:** 3 dias após o envio deste teste por e-mail.

---

## ✅ Checklist do participante (o que não pode faltar)
- [ ] Fork e branch com nome correto (`nome-sobrenome`)  
- [ ] `RESPOSTAS.md` com respostas claras e sinceras  
- [ ] Código do servidor em `src/` funcionando localmente  
- [ ] `docs/DOCUMENTACAO.md` explicando decisões e raciocínio  
- [ ] Instruções de execução passo a passo (como rodar e testar)  
- [ ] Declaração clara sobre o uso (ou não) de IA e onde ela foi usada  
- [ ] Código organizado e legível; commits significativos

---

## 🧾 Critérios de avaliação
A avaliação será feita considerando:

- **Clareza e sinceridade** das respostas teóricas.  
- **Funcionamento** do servidor (testes manuais básicos devem passar).  
- **Qualidade do código:** organização, legibilidade, boas práticas.  
- **Metodologias utilizadas:** testes, versionamento, padrões aplicados.  
- **Documentação:** explicativa, com passo a passo para rodar/testar.  
- **Justificativa do uso de IA:** se usada, deve estar declarada e explicada.

---

## 🗣 Observações finais
- Valoramos **transparência**: se usou IA em qualquer parte, declare com qual ferramenta e o que foi gerado por ela.  
- Queremos compreender **seu raciocínio** — não apenas o resultado final.  
- Perguntas (dúvidas sobre o teste) podem ser feitas por e-mail antes do prazo final.  
- Boa sorte — esperamos ver seu raciocínio e competência! 🚀
