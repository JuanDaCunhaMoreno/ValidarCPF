# 🧾 Validador de CPF em Python

Um validador de CPF simples, funcional e interativo via terminal.  
Digite quantos CPFs quiser e descubra se são válidos segundo as regras da Receita Federal.

---

## 📌 Funcionalidades

- ✅ Validação real dos dígitos verificadores do CPF
- 🔁 Laço contínuo (`while True`) para testar vários CPFs
- 🧼 Aceita entrada com ou sem formatação (`12345678909` ou `123.456.789-09`)
- 🟥 Feedback visual com cores no terminal (verde/vermelho)
- ❌ Bloqueia CPFs inválidos como `111.111.111-11` ou `000.000.000-00`
- 💬 Comando `sair` para encerrar o programa

---

## 🧠 Como funciona

A função `validar_cpf()`:
1. Remove caracteres não numéricos do CPF.
2. Verifica se tem 11 dígitos.
3. Rejeita CPFs com todos os números iguais.
4. Calcula corretamente os dois dígitos verificadores.
5. Retorna `True` ou `False` de acordo com a validade do CPF.

---

## 🗂 Estrutura do Projeto

validador_cpf/
├── main.py # Entrada principal do usuário com loop e cores
├── validador.py # Função para validação do CPF
├── utils.py # Função cor() para colorir os prints (opcional)
└── README.md # Documentação do projeto

