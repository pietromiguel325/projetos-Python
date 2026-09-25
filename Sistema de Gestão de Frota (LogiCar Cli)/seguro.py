class Seguro:
    def calcular_taxa_seguro(self, dias: int):
        return 0.0

class SeguroBasico(Seguro):
    def calcular_taxa_seguro(self, dias: int):
        return dias * 20

class SeguroPremium(Seguro):
    def calcular_taxa_seguro(self, dias: int):
        return dias * 50