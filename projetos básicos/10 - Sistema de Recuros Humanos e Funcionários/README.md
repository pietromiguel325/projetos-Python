# 👥 Desafio 10: Sistema de Recursos Humanos e Funcionários

Um sistema em console desenvolvido em Python para gestão de recursos humanos, controlo de folha salarial e análise estatística de colaboradores ativos por setor[cite: 8, 24].

---

## 📌 Funcionalidades

- **Gestão de Colaboradores**:
  - Registo de novos funcionários com ID automático via `random`[cite: 24].
  - Alteração salarial com validação de estado ativo do funcionário[cite: 24].
  - Desligamento/Demissão de colaboradores (alteração de estado para inativo)[cite: 24].
- **Consultas e Relatórios**:
  - Listagem geral e visualização exclusiva de funcionários ativos[cite: 24].
  - Busca individual por ID com tratamento e validação de dados de entrada[cite: 24].
- **Métricas Financeiras e de RH**:
  - Cálculo da folha salarial total considerando apenas funcionários ativos[cite: 24].
  - Identificação do maior salário entre os colaboradores ativos[cite: 24].
  - Distribuição quantitativa de funcionários ativos agrupados por setor[cite: 24].
  - Cálculo da média salarial individualizada por setor[cite: 24].

---

## 💻 Tecnologias e Conceitos Utilizados

- **Python 3**[cite: 24]
- **Tratamento de Exceções**: Blocos `try/except` com `ValueError` para assegurar a introdução válida de salários[cite: 24].
- **Dicionários Aninhados & Dicionários por Compreensão**: Utilizados para acumulação de somas e contagens na geração da média salarial por setor[cite: 24].
- **Padronização de Dados**: Uso de `.strip()`, `.capitalize()`, `.replace()` e `.lower()` para higienização e compatibilidade de texto (ex: conversão de vírgulas para pontos em salários)[cite: 24].
- **Funções Callback**: Utilização do padrão de callback em `verificar_busca` para aplicar alterações salariais ou demissões de forma dinâmica[cite: 24].

---

## 🛠️ Como Executar

1. Certifica-te de que tens o **Python 3** instalado[cite: 24].
2. Navega até à pasta do projeto:
   ```bash
   cd "10 - Sistema de Recursos Humanos e Funcionários"