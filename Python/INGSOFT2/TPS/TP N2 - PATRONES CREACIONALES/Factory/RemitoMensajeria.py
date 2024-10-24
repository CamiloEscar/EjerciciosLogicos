from Factory import Creator
from Product import Product

class RemitoMensajeria(Creator):
    def factory_method(self) -> Product:
        return CrearRemitoMensajeria()

class CrearRemitoMensajeria(Product):
    def operation(self) -> str:
        return "REMITO POR MENSAJERIA"