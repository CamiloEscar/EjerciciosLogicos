from tokenize import Double
from xmlrpc.client import boolean
from Tarjeta import Tarjeta


class TarjetaCredito(Tarjeta):
    def getimpuesto(self):
        return 100

    def puedePagarEnCuotas(self) -> boolean:
        return True

    def ingresarDinero(self, monto: Double) -> Double:
        return monto - self.getimpuesto()