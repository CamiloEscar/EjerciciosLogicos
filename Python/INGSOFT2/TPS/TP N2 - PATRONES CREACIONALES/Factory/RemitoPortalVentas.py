from Factory import Creator
from Product import Product

class RemitoPortalVentas(Creator):
    def factory_method(self) -> Product:
        return CrearRemitoPortalVentas()

class CrearRemitoPortalVentas(Product):
    def operation(self) -> str:
        return "REMITO POR VENTAS"