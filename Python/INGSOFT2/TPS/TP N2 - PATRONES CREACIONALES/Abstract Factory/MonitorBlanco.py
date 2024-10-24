from numpy import double
from AbstractProductMonitor import AbstractProductMonitor

class MonitorBlanco(AbstractProductMonitor):
    def getNombre(self) -> str:
        return "Monitor"
    
    def getColor(self) -> str:
        return "Blanco"

    def getResolucion(self) -> str:
        return "1080p"
    
    def getCosto(self) -> double:
        return 2000.00