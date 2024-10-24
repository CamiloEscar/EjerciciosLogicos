from abc import ABC, abstractmethod
from AbstractFactory import AbstractFactory
from AbstractProductMonitor import AbstractProductMonitor
from AbstractProductMouse import AbstractProductMouse
from AbstractProductTeclado import AbstractProductTeclado
from MonitorBlanco import MonitorBlanco
from MouseBlanco import MouseBlanco
from TecladoBlanco import TecladoBlanco

class ConcreteFactorySetUpBlanco(AbstractFactory):
    def create_product_a(self) -> AbstractProductMonitor:
        return MonitorBlanco()

    def create_product_b(self) -> AbstractProductMouse:
        return MouseBlanco()

    def create_product_c(self) -> AbstractProductTeclado:
        return TecladoBlanco()