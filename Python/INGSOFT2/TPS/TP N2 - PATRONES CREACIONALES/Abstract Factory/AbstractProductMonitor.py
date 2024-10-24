from abc import ABC, abstractmethod

from numpy import double

class AbstractProductMonitor(ABC):
    @abstractmethod
    def getNombre(self) -> str:
        pass

    @abstractmethod
    def getColor(self) -> None:
        pass
    
    @abstractmethod
    def getResolucion(self) -> str:
        pass

    @abstractmethod
    def getCosto(self) -> double:
        pass