from seguro import Seguro
from exceptions import VeiculoIndisponivelError, DadosInvalidosError, VeiculoNaoAlugadoError

class Veiculo: 
    def __init__(self, placa: str, modelo: str, valor_diaria: float, seguro: Seguro, km_rodado: float = 0.0):
        self.placa = placa 
        self.modelo = modelo 
        self.valor_diaria = valor_diaria 
        self.seguro = seguro 
        self._alugado = False 
        self._km_rodado = km_rodado 

    @property
    def alugado(self): 
        return self._alugado 

    @property
    def km_rodado(self): 
        return self._km_rodado 

    def alugar(self): 
        if self._alugado: 
            raise VeiculoIndisponivelError(f"O veículo {self.placa} já está alugado!") 
        self._alugado = True 
        print("O Veículo foi Alugado!") 
        return True 

    def devolver(self, km_percorridos: float): 
        if km_percorridos < 0: 
            raise DadosInvalidosError(f"Valor Inválido! [ERRO] KM | Tentativa: {km_percorridos}")
        if self._alugado: 
            self._km_rodado += km_percorridos 
            print("O Veículo foi Devolvido!") 
            self._alugado = False 
            return True 
        raise VeiculoNaoAlugadoError(f"O veículo {self.placa} não está alugado!")

    def calcular_aluguel(self, dias: int):
        if dias < 0:
            raise DadosInvalidosError(f"Valor Inválido! [ERRO] DIAS | Tentativa: {dias}")
        return self.valor_diaria * dias

    def calcular_aluguel_seguro(self, dias: int):
        aluguel_veiculo = self.calcular_aluguel(dias)
        taxa_seguro = self.seguro.calcular_taxa_seguro(dias)
        return aluguel_veiculo + taxa_seguro


class CarroPasseio(Veiculo):
    def __init__(self, placa: str, modelo: str, valor_diaria: float, seguro: Seguro, km_rodado: float = 0.0):
        super().__init__(placa, modelo, valor_diaria, seguro, km_rodado)

    def calcular_aluguel(self, dias: int):
        if dias < 0:
            raise DadosInvalidosError(f"Valor Inválido! [ERRO] DIAS | Tentativa: {dias}")
        aux = super().calcular_aluguel(dias)
        if dias > 7:
            aux *= 0.90
        return aux


class Caminhao(Veiculo):
    def __init__(self, placa: str, modelo: str, valor_diaria: float, seguro: Seguro, capacidade_carga_ton: float, km_rodado: float = 0.0):
        super().__init__(placa, modelo, valor_diaria, seguro, km_rodado)
        self.capacidade_carga_ton = capacidade_carga_ton

    def calcular_aluguel(self, dias: int):
        if dias < 0:
            raise DadosInvalidosError(f"Valor Inválido! [ERRO] DIAS | Tentativa: {dias}")
        aluguel_base = super().calcular_aluguel(dias)
        taxa_carga = self.capacidade_carga_ton * 50.0
        return aluguel_base + taxa_carga