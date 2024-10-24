from tokenize import Double
from xmlrpc.client import boolean
from Tarjeta import Tarjeta


class Decorator(Tarjeta):
    _tarjeta: Tarjeta = None

    def __init__(self, tarjeta: Tarjeta) -> None:
        self._tarjeta = tarjeta
    
    @property
    def tarjeta(self):
        return self._tarjeta

    def getimpuesto(self) -> Double:
        return self._tarjeta.getimpuesto(self)

    def puedePagarEnCuotas(self) -> boolean:
        return self._tarjeta.puedePagarEnCuotas()

    def ingresarDinero(self, monto: Double) -> Double:
        return self._tarjeta.ingresarDinero(monto)

    