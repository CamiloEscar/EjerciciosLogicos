from __future__ import annotations
from abc import ABC, abstractmethod
from tokenize import Double
from xmlrpc.client import boolean



class Tarjeta(ABC):
    
    def getimpuesto(self):
        pass

    def puedePagarEnCuotas(self) -> boolean:
        pass

    def ingresarDinero(self, monto: Double) -> Double:
        pass