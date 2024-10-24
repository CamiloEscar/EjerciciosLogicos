from abc import ABC, abstractmethod

from numpy import double
from AbstractProductMonitor import AbstractProductMonitor

class AbstractProductMouse(ABC):
    @abstractmethod
    def getNombre(self) -> None:
        pass

    @abstractmethod
    def getColor(self) -> None:
        pass

    @abstractmethod
    def getDPI(self) -> None:
        pass

    @abstractmethod
    def getCosto(self) -> double:
        pass