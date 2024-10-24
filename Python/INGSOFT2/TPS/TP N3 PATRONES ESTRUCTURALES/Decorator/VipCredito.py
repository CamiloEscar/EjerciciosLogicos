from tokenize import Double
from Decorator import Decorator
from Tarjeta import Tarjeta


class VipCredito(Decorator):
    def __init__(self, tarjeta: Tarjeta) -> None:
        super().__init__(tarjeta)
        
    def ingresarDinero(self, monto: Double) -> Double:
        return self._tarjeta.ingresarDinero(self, monto) + self.getimpuesto()