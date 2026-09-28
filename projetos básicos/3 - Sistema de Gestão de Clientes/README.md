# 👥 Desafio 3: Sistema de Gestão de Clientes

Um sistema CRUD (Create, Read, Update, Delete) interativo em consola desenvolvido em Python para gestão e manutenção de registos de clientes.

---

## 📌 Funcionalidades

- **Listagem Geral**: Apresenta todos os clientes registados com ID, nome, e-mail e idade.
- **Busca por ID**: Localiza registos específicos na lista utilizando filtragem funcional.
- **Registo Dinâmico**: Adiciona novos clientes gerando automaticamente o próximo ID disponível.
- **Atualização de Dados**: Permite editar nome, e-mail e idade de um cliente existente.
- **Remoção com Confirmação**: Exclui registos da lista garantindo validação de segurança (S/N).

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**
- **Estruturas de Controlo**: Menu interativo com `while True` e estrutura de seleção `match/case`.
- **Programação Funcional**: Utilização de `filter()` e expressões `lambda`.
- **Tratamento de Strings**: Funções `.strip()` e `.upper()` para higienização e validação de dados introduzidos pelo utilizador.
- **Manipulação de Coleções**: Adição (`.append()`) e remoção (`.remove()`) de elementos em listas de dicionários.

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado.
2. Navega até à pasta do projeto:
   ```bash
   cd "3 - Sistema de Gestão de Clientes"