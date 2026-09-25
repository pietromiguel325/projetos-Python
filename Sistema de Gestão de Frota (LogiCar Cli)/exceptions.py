class LocadoraException(Exception):
    pass

class VeiculoIndisponivelError(LocadoraException):
    pass

class VeiculoNaoAlugadoError(LocadoraException):
    pass

class DadosInvalidosError(LocadoraException):
    pass