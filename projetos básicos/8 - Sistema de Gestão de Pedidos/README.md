# 🛒 Desafio 8: Sistema de Gestão de Pedidos

Um sistema interativo desenvolvido em Python para gestão do ciclo de vida de pedidos de vendas, processamento financeiro e análise de métricas por cliente e categoria[cite: 6, 22].

---

## 📌 Funcionalidades

- **Gestão do Ciclo de Pedidos**:
  - Registo de novos pedidos com ID dinâmico e estado inicial `Processando`[cite: 22].
  - Alteração de estados (`Processando`, `Enviado`, `Entregue`, `Cancelado`)[cite: 22].
  - Regra de cancelamento: Impede o cancelamento de pedidos que já tenham sido marcados como `Entregue`[cite: 22].
- **Métricas Financeiras Ignorando Cancelados**:
  - Cálculo de faturamento total desconsiderando vendas canceladas[cite: 22].
  - Agrupamento de faturamento por categoria de produto[cite: 22].
  - Identificação do pedido válido de maior valor financeiro[cite: 22].
- **Consultas e Relatórios**:
  - Listagem geral e busca direcionada por ID[cite: 22].
  - Filtragem por estado do pedido[cite: 22].
  - Identificação do cliente com maior volume financeiro consumido (*Cliente que mais gastou*)[cite: 22].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 22]
- **Validação de Inputs**: Validação com `.isdigit()` para garantir quantidades e opções válidas do utilizador[cite: 22].
- **Regras de Negócio em Funções**: Filtros com *List Comprehension* para ignorar transações canceladas no cálculo das métricas[cite: 22].
- **Agregação Dinâmica**: Uso do `max()` com expressão `lambda` sobre o método `.items()` para identificar o cliente líder em vendas[cite: 22].
- **Estruturas de Controlo**: Menu em consola com `while True` e estrutura `match/case`[cite: 22].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 22].
2. Navega até à pasta do projeto:
   ```bash
   cd "8 - Sistema de Gestão de Pedidos"