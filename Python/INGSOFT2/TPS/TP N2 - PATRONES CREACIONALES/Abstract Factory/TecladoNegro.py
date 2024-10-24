from numpy import double
from AbstractProductTeclado import AbstractProductTeclado

class TecladoNegro(AbstractProductTeclado):
    def getNombre(self) -> str:
        return "Teclado"

    def getColor(self) -> str:
        return "Negro"

    def getIdioma(self) -> str:
        return "Ingles"

    def getPorcentajeTeclas(self) -> int:
        return 80
    
    def getCosto(self) -> double:
        return 1200.00