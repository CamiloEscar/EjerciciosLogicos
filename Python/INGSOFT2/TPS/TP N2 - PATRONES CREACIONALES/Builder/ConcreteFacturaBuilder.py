from IFacturaBuilder import IFacturaBuilder
from Factura import Factura

class ConcreteFacturaBuilder(IFacturaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._factura = Factura()

    @property
    def factura(self) -> Factura:
        factura = self._factura
        self.reset()
        return factura
    
    def dirCorreoElectronico(self, dirCorreo) -> None:
        self._factura.add(dirCorreo)
    
    def numeroTelefonico(self, numero) -> None:
        self._factura.add(numero)

    def personaContacto(self, pContacto) -> None:
       self._factura.add(pContacto)
    
    def nombreComercial(self, nombre) -> None:
        self._factura.add(nombre)
    
    def numeroComprobante(self, numero) -> None:
        self._factura.add(numero)
    
    def domicilioComercial(self, domicilio) -> None:
        self._factura.add(domicilio)

    def nombreEmisor(self, nombre) -> None:
        self._factura.add(nombre)

    def rfcEmisor(self, rfc) -> None:
        self._factura.add(rfc)

    def nombreReceptor(self, nombre) -> None:
        self._factura.add(nombre)

    def rfcReceptor(self, rfc) -> None:
        self._factura.add(rfc)

    def folioFiscalDigital(self, folioFiscalDigital) -> None:
        self._factura.add(folioFiscalDigital)

    def fechaEmisor(self, fecha) -> None:
        self._factura.add(fecha)
    
    def lugarEmisor(self, lugar) -> None:
        self._factura.add(lugar)
    
    def horaEmisor(self, hora) -> None:
        self._factura.add(hora)

    def tipoCfdi(self, tipoCfdi) -> None:
        self._factura.add(tipoCfdi)

