# 🛠️ Desafio 11: Sistema de Chamados e Suporte Técnico

Um sistema em console desenvolvido em Python para gestão e monitorização de chamados de suporte técnico, com recursos de filtragem por estado, níveis de prioridade e estatísticas de atendimento[cite: 9, 25].

---

## 📌 Funcionalidades

- **Abertura e Atualização de Chamados**:
  - Registo de novos chamados com atribuição automática de ID único via `random`[cite: 25].
  - Alteração de estado (`Aberto`, `Em andamento`, `Resolvido`) com validação[cite: 25].
- **Consultas e Filtros**:
  - Busca direcionada por ID com validação de dados de entrada[cite: 25].
  - Listagem de chamados filtrados por estado ou por prioridade[cite: 25].
- **Relatórios e Métricas**:
  - Contagem quantitativa de chamados agrupados por categoria e por estado[cite: 25].
  - Identificação automatizada do chamado de maior urgência (baseado em pesos de prioridade)[cite: 25].
  - Identificação do cliente com maior número de solicitações abertas[cite: 25].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 25]
- **Pesos de Prioridade**: Dicionário de conversão de texto para valores numéricos (`"Alta": 3, "Média": 2, "Baixa": 1`) integrado com a função `max()`[cite: 25].
- **Funções Callback**: Utilização do padrão em `verificar_buscar` para associar ações de atualização aos chamados localizados[cite: 25].
- **Tratamento de Dados**: Validações numéricas e higienização de strings com `.strip()` e `.capitalize()`[cite: 25].
- **Estruturas de Controlo**: Menu interativo em console com `while True` e `match/case`[cite: 25].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 25].
2. Navega até à pasta do projeto:
   ```bash
   cd "11 - Sistema de Chamados e Suporte Técnico"