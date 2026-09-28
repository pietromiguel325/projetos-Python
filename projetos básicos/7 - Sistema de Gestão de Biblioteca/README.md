# 📚 Desafio 7: Sistema de Gestão de Biblioteca

Um sistema em consola desenvolvido em Python para gestão de acervo bibliográfico, controlo de empréstimos e devoluções, e consultas avançadas por autor, categoria e publicação[cite: 5, 21].

---

## 📌 Funcionalidades

- **Controlo de Acervo**:
  - Registo de novos livros com geração dinâmica de ID único via `random`[cite: 21].
  - Empréstimo e devolução de obras com atualização imediata de estado (`disponivel`)[cite: 21].
- **Consultas e Pesquisas**:
  - Listagem completa do acervo e visualização exclusiva de obras disponíveis[cite: 21].
  - Busca de livros por ID ou por autor (com correspondência case-insensitive)[cite: 21].
- **Estatísticas do Acervo**:
  - Apuração da quantidade de obras agrupadas por categoria[cite: 21].
  - Identificação automatizada do livro mais antigo e do mais recente[cite: 21].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 21]
- **Passagem de Funções como Parâmetro**: Callback funcional na função `verificar_busca` para executar ações de empréstimo/devolução dinamicamente[cite: 21].
- **Funções de Agregação**: Uso de `min()` e `max()` com `lambda` para comparar os anos de publicação[cite: 21].
- **Tratamento de Strings**: Aplicação de `.title()`, `.capitalize()`, `.strip()` e `.lower()` para padronização de buscas e cadastros[cite: 21].
- **Estruturas de Controlo**: Menu interativo utilizando `while True` e `match/case`[cite: 21].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 21].
2. Navega até à pasta do projeto:
   ```bash
   cd "7 - Sistema de Gestão de Biblioteca"