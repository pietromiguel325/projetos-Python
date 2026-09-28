# 🏭 Desafio 9: Sistema de Controlo de Estoque Avançado

Um sistema em console desenvolvido em Python para gestão abrangente de inventários, movimentação de mercadorias e relatórios financeiros detalhados por categoria e produto[cite: 7, 23].

---

## 📌 Funcionalidades

- **Operações de Estoque**:
  - Registo de novos produtos com geração automática de ID único (1 a 100)[cite: 23].
  - Registo de entrada e saída de estoque com verificação de disponibilidade[cite: 23].
  - Validação de IDs introduzidos pelo utilizador através de loop de verificação[cite: 23].
- **Filtros e Alertas**:
  - Identificação de produtos com estoque crítico (menor ou igual a 5 unidades)[cite: 23].
  - Busca de produtos por ID com exibição detalhada[cite: 23].
- **Relatórios Financeiros e Estatísticas**:
  - Cálculo do valor total imobilizado no estoque[cite: 23].
  - Agrupamento e cálculo do valor financeiro por categoria[cite: 23].
  - Localização automatizada do produto com maior volume em estoque e do produto mais caro[cite: 23].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 23]
- **Passagem de Funções Callback**: Reutilização da função `verificar_buscar` passando funções de movimentação (`adicionar_estoque` e `saida_estoque`) como parâmetro[cite: 23].
- **Expressões Lambda & `max()`**: Utilizadas para identificar o produto de maior estoque e o produto com maior preço unitário[cite: 23].
- **Validação de Dados**: Uso de `.isdigit()` e validação numérica para garantir limites válidos de ID e quantidade[cite: 23].
- **Estrutura de Decisão e Repetição**: Menu interativo com `while True` e `match/case`[cite: 23].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 23].
2. Navega até à pasta do projeto:
   ```bash
   cd "9 - Sistema de Controle de Estoque Avancado"