from numpy import double
from AbstractProductMonitor import AbstractProductMonitor

class MonitorNegro(AbstractProductMonitor):
    def getNombre(self) -> str:
        return "Monitor"
    
    def getColor(self) -> str:
        return "Negro"

    def getResolucion(self) -> str:
        return "1080p"
    
    def getCosto(self) -> double:
        return 1500.00