from numpy import double
from AbstractProductMouse import AbstractProductMouse

class MouseBlanco(AbstractProductMouse):
    def getNombre(self) -> str:
        return "Mouse"

    def getColor(self) -> str:
        return "Blanco"

    def getDPI(self) -> int:
        return 6000
    
    def getCosto(self) -> double:
        return 100.00