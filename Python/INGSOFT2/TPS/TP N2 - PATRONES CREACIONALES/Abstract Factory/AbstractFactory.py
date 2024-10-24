from __future__ import annotations
from abc import ABC, abstractmethod
from AbstractProductMonitor import AbstractProductMonitor
from AbstractProductMouse import AbstractProductMouse
from AbstractProductTeclado import AbstractProductTeclado

class AbstractFactory(ABC):
    @abstractmethod
    def crear_producto_a(self) -> AbstractProductMonitor:
        pass

    @abstractmethod
    def crear_producto_b(self) -> AbstractProductMouse:
        pass

    def crear_producto_c(self) -> AbstractProductMouse:
        pass