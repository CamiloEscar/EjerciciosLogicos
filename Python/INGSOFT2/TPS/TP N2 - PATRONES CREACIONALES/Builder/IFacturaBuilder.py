from abc import ABC, abstractmethod

class IFacturaBuilder(ABC):

    @property
    @abstractmethod
    def factura(self) -> None:
        pass

    @abstractmethod
    def nombreEmisor(self, nombre) -> None:
        pass

    @abstractmethod
    def rfcEmisor(self, rfc) -> None:
        pass

    @abstractmethod
    def nombreReceptor(self, nombre) -> None:
        pass

    @abstractmethod
    def rfcReceptor(self, rfc) -> None:
        pass
    
    @abstractmethod
    def folioFiscalDigital(self, folioFiscalDigital) -> None:
        pass

    @abstractmethod
    def fechaEmisor(self, fecha) -> None:
        pass
    
    @abstractmethod
    def lugarEmisor(self, lugar) -> None:
        pass
    
    @abstractmethod
    def horaEmisor(self, hora) -> None:
        pass

    @abstractmethod
    def tipoCfdi(self, tipoCfdi) -> None:
        pass
    
    @abstractmethod
    def domicilioComercial(self, domicilio) -> None:
        pass

    @abstractmethod
    def dirCorreoElectronico(self, dirCorreo) -> None:
        pass
    
    @abstractmethod
    def numeroTelefonico(self, numero) -> None:
        pass

    @abstractmethod
    def personaContacto(self, pContacto) -> None:
        pass
    
    @abstractmethod
    def nombreComercial(self, nombre) -> None:
        pass
    
    @abstractmethod
    def numeroComprobante(self, numero) -> None:
        pass
    
    