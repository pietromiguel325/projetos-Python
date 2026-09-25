class Auditoria:
    faturamento_total = 0.0
    historico = []

    @classmethod
    def registrar_locacao(cls, veiculo, dias: int, valor_total: float):
        cls.faturamento_total += valor_total
        cls.historico.append(f"Placa: {veiculo.placa} | Dias: {dias} | Valor Total: R${valor_total:.2f}")

    @classmethod
    def exibir_balanco(cls):
        print("=== RELATÓRIO LOCAÇÃO ===")
        for op in cls.historico:
            print(op)
        print(f"\nFaturamento Total Acumulado: R${cls.faturamento_total:.2f}")