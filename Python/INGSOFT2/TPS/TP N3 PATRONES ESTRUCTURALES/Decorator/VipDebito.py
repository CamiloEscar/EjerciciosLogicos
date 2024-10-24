from tokenize import Double
from xmlrpc.client import boolean
from Decorator import Decorator


class VipDebito(Decorator):

    def ingresarDinero(self, monto: Double) -> Double:
        return self._tarjeta.ingresarDinero(self, monto) + self.getimpuesto() * 0.50
    
    def puedePagarEnCuotas(self) -> boolean:
        return True