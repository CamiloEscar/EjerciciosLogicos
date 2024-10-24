from abc import ABC, abstractmethod
from AbstractFactory import AbstractFactory
from AbstractProductMonitor import AbstractProductMonitor
from AbstractProductMouse import AbstractProductMouse
from AbstractProductTeclado import AbstractProductTeclado
from MonitorBlanco import MonitorBlanco
from MonitorNegro import MonitorNegro
from MouseBlanco import MouseBlanco
from MouseNegro import MouseNegro
from TecladoBlanco import TecladoBlanco
from TecladoNegro import TecladoNegro

class ConcreteFactorySetUpNegro(AbstractFactory):
    def create_product_a(self) -> AbstractProductMonitor:
        return MonitorNegro()

    def create_product_b(self) -> AbstractProductMouse:
        return MouseNegro()

    def create_product_c(self) -> AbstractProductTeclado:
        return TecladoNegro()