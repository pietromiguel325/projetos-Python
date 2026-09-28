# 🏥 Desafio 12: Sistema de Agendamento da Clínica Médica

Um sistema em console desenvolvido em Python para gestão de consultas médicas, controlo de estados de agendamento e análise estatística de atendimentos e faturamento[cite: 10, 26].

---

## 📌 Funcionalidades

- **Gestão de Agendamentos**:
  - Registo de novos agendamentos com id gerado dinamicamente via `random` e estado inicial `Agendado`[cite: 26].
  - Alteração de estado (`Agendado`, `Realizado`, `Cancelado`) com validação de opções[cite: 26].
- **Consultas e Filtros**:
  - Busca direcionada por ID com tratamento de dados[cite: 26].
  - Listagem de consultas filtradas por estado ou especialidade médica[cite: 26].
- **Métricas Financeiras e Estatísticas**:
  - Cálculo do faturamento total acumulado apenas de consultas com estado `Realizado`[cite: 26].
  - Contagem do número de atendimentos por médico[cite: 26].
  - Identificação da consulta de maior valor financeiro[cite: 26].
  - Destaque do médico com mais consultas e do paciente com maior número de agendamentos[cite: 26].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 26]
- **Tratamento de Exceções**: Bloco `try/except` com `ValueError` para garantir a introdução correta de valores monetários positivos[cite: 26].
- **Set Comprehension**: Utilizado para extrair dinamicamente a lista de especialidades únicas existentes no acervo (`{agendamento['especialidade'].lower() ...}`)[cite: 26].
- **Agregação com `max()`**: Aplicação de expressões `lambda` em dicionários e tuplas (`.items()`) para determinar recordes de consultas e faturamento[cite: 26].
- **Estruturas de Controlo**: Menu interativo em console construído com `while True` e `match/case`[cite: 26].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 26].
2. Navega até à pasta do projeto:
   ```bash
   cd "12 - Sistema de Agendamento de Clínica Médica"