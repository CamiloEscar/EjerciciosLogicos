from ImpresorFrameHDMI import ImpresorFrameHDMI
from ImpresorFrameDVI import ImpresorFrameDVI

class ImpresorFraneDVIAdapter(ImpresorFrameHDMI, ImpresorFrameDVI):
    def conversorResolucion(self) -> str:
        dic_resolucion = {"1080": "1920x1080",
                          "720": "1280x720",
                          "480": "640x480"}
        
        return dic_resolucion[self.getResolucion()]

    def imprimir(self, frame) -> str:
        resolucion = self.conversorResolucion()
        print(frame + ' ' + resolucion)