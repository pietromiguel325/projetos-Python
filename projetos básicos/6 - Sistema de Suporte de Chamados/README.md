# 🎫 Desafio 6: Sistema de Suporte de Chamados

Um sistema em consola desenvolvido em Python para gestão de bilhetes de suporte/chamados técnicos, permitindo abertura, acompanhamento, filtragem e alteração de estados de atendimento[cite: 4, 20].

---

## 📌 Funcionalidades

- **Registo e Gestão**:
  - Abertura de novos chamados com geração automática de ID único via `random`[cite: 20].
  - Atualização do estado dos chamados (Aberto, Em andamento, Resolvido)[cite: 20].
  - Encerrar chamados com validação de confirmação do utilizador[cite: 20].
- **Consultas e Filtros**:
  - Listagem geral e busca direcionada por ID[cite: 20].
  - Filtragem de chamados por prioridade ou estado[cite: 20].
- **Métricas e Regras de Negócio**:
  - Contagem total de chamados agrupados por categoria[cite: 20].
  - Identificação do chamado de maior prioridade através de mapeamento numérico (pesos de prioridade)[cite: 20].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 20]
- **Mapeamento de Pesos (De-Para)**: Dicionário para conversão de texto em valores numéricos (`"Baixa": 1, "Média": 2, "Alta": 3`) para ordenação com `max()`[cite: 20].
- **Tratamento de Strings**: Funções `.capitalize()`, `.strip()` e `.lower()` para padronização da entrada de dados[cite: 20].
- **Estruturas de Controlo**: Menu interativo com `while True` e `match/case`[cite: 20].
- **List Comprehension**: Para validação e verificação de IDs ativos[cite: 20].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 20].
2. Navega até à pasta do projeto:
   ```bash
   cd "6 - Sistema de Suporte de Chamados"