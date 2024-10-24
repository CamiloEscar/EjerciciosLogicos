from abc import ABC, abstractmethod

from numpy import double

class AbstractProductTeclado(ABC):
    @abstractmethod
    def getNombre(self) -> None:
        pass

    @abstractmethod
    def getColor(self) -> None:
        pass

    @abstractmethod
    def getIdioma(self) -> None:
        pass

    @abstractmethod
    def getPorcentajeTeclas(self) -> None:
        pass

    @abstractmethod
    def getCosto(self) -> double:
        pass