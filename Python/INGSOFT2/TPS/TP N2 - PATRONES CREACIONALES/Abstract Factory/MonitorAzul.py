from numpy import double
from AbstractProductMonitor import AbstractProductMonitor

class MonitorAzul(AbstractProductMonitor):
    def getNombre(self) -> str:
        return "Monitor"
    
    def getColor(self) -> str:
        return "Azul"

    def getResolucion(self) -> str:
        return "1080p"
    
    def getCosto(self) -> double:
        return 4000.00