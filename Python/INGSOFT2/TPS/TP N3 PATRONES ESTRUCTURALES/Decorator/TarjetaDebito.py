from tokenize import Double
from xmlrpc.client import boolean
from Tarjeta import Tarjeta

class TarjetaDebito(Tarjeta):
    def getimpuesto(self) -> Double:
        return 200

    def puedePagarEnCuotas(self) -> boolean:
        return False

    def ingresarDinero(self, monto: Double) -> Double:
        return monto - self.getimpuesto()