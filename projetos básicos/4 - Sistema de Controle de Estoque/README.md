# 📦 Desafio 4: Sistema de Controlo de Estoque

Um sistema interativo em consola desenvolvido em Python para gestão de inventário, controlo de movimentações de entrada/saída de produtos e cálculo de métricas financeiras de estoque.

---

## 📌 Funcionalidades

- **Listagem e Busca**: Visualização geral de produtos ou procura individual por ID.
- **Registo Dinâmico com ID Único**: Registo de produtos com geração de IDs aleatórios não repetidos via biblioteca `random`.
- **Movimentação de Estoque**:
  - **Entrada**: Soma novas unidades ao estoque atual.
  - **Saída**: Subtrai quantidades com verificação de segurança para evitar saldo negativo.
- **Alertas de Nível Crítico**: Filtro para identificar produtos com unidades em nível crítico (estoque inferior a 5).
- **Valoração de Inventário**: Cálculo automatizado do valor total acumulado no estoque por item e no valor geral.

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**
- **Módulos Nativos**: Utilização do `randint` do módulo `random` para atribuição de IDs.
- **Estruturas de Controlo**: Menu interativo com `while True` e estrutura `match/case`.
- **List Comprehension**: Para mapeamento e verificação de IDs existentes na lista.
- **Modularização**: Separação das regras de negócio em funções exclusivas (`def`).

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado.
2. Navega até à pasta do projeto:
   ```bash
   cd "4 - Sistema de Controlo de Estoque"