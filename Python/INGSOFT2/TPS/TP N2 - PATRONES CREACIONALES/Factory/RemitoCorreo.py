from Factory import Creator
from Product import Product

class RemitoCorreo(Creator):
    def factory_method(self) -> Product:
        return CrearRemitoCorreo()

class CrearRemitoCorreo(Product):
    def operation(self) -> str:
        return "REMITO POR CORREO"