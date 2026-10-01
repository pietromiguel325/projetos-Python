# 🚗 Sistema de Gestão de Frota (LogiCar CLI)

Sistema em Python desenvolvido para gerenciar a frota, locações e financeiro de uma locadora de veículos via interface de linha de comando (CLI).

## 📌 Funcionalidades
- **Cadastro de Veículos:** Suporte a carros de passeio e caminhões.
- **Gestão de Locações:** Controle de aluguel e devolução com cálculo de diárias e taxa de seguro.
- **Integração de Seguros:** Suporte a seguro básico e premium com regras dinâmicas.
- **Relatório & Auditoria:** Acompanhamento do faturamento total e status da frota.

## 🛠️ Conceitos e Tecnologias
- **POO (Programação Orientada a Objetos):** Encapsulamento (`@property`), Herança, Composição de classes e Abstração.
- **Código Defensivo:** Exceções customizadas (`LocadoraException`), tratamento com `try/except` e validação rigorosa de entradas.
- **Estruturas de Controle:** Controle de fluxo dinâmico com `match/case` e loops de validação `while`.
- **Arquitetura Modular:** Separação de responsabilidades em múltiplos arquivos `.py`.

## 📂 Estrutura do Projeto
- `main.py` - Interface CLI e fluxo principal do sistema.
- `veiculo.py` - Classe base `Veiculo` e subclasses (`CarroPasseio`, `Caminhao`).
- `seguro.py` - Módulo de seguros (`SeguroBasico`, `SeguroPremium`).
- `exceptions.py` - Hierarquia de erros e exceções personalizadas.
- `auditoria.py` - Controle financeiro centralizado com `@classmethod`.

## 🚀 Como Executar
1. Certifique-se de ter o Python 3.10+ instalado.
2. Baixe os arquivos.

