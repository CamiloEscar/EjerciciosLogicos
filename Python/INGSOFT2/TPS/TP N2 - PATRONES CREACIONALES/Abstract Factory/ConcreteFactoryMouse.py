from AbstractFactory import AbstractFactory
from AbstractProductMouse import AbstractProductMouse
from MouseBlanco import MouseBlanco
from MouseNegro import MouseNegro

class ConcreteFactoryMouse(AbstractFactory):
    def crear_producto_a(self) -> AbstractProductMouse:
        return MouseBlanco()
    
    def crear_producto_b(self) -> AbstractProductMouse:
        return MouseNegro()

    def crear_producto_c(self) -> AbstractProductMouse:
        pass
