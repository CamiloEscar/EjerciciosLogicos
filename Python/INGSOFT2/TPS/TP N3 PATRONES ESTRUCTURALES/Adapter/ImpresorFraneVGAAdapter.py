from ImpresorFrameHDMI import ImpresorFrameHDMI
from ImpresorFrameVGA import ImpresorFrameVGA

class ImpresorFraneVGAAdapter(ImpresorFrameHDMI, ImpresorFrameVGA):
    def conversorResolucion(self) -> str:
        resolucionX, resolucionY = self.getResolucion()
        return [resolucionY, resolucionX]

    def imprimir(self, frame) -> str:
        resolucionYX = self.conversorResolucion()
        resolucion = (resolucionYX[0] + 'x' + resolucionYX[1])
        print(frame + ' ' + resolucion)