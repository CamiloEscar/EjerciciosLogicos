from numpy import double
from AbstractProductMouse import AbstractProductMouse

class MouseNegro(AbstractProductMouse):
    def getNombre(self) -> str:
        return "Mouse"

    def getColor(self) -> str:
        return "Negro"

    def getDPI(self) -> int:
        return 4230
    
    def getCosto(self) -> double:
        return 50.00