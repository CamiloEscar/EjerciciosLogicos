from numpy import double
from AbstractProductTeclado import AbstractProductTeclado

class TecladoBlanco(AbstractProductTeclado):
    def getNombre(self) -> str:
        return "Teclado"

    def getColor(self) -> str:
        return "Blanco"

    def getIdioma(self) -> str:
        return "Español"

    def getPorcentajeTeclas(self) -> int:
        return 60
    
    def getCosto(self) -> double:
        return 1400.00