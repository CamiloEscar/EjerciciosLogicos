from AbstractFactory import AbstractFactory
from AbstractProductTeclado import AbstractProductTeclado
from TecladoBlanco import TecladoBlanco
from TecladoNegro import TecladoNegro

class ConcreteFactoryTeclado(AbstractFactory):
    def crear_producto_a(self) -> AbstractProductTeclado:
        return TecladoBlanco()
    
    def crear_producto_b(self) -> AbstractProductTeclado:
        return TecladoNegro()
    
    def crear_producto_c(self) -> AbstractProductTeclado:
        pass