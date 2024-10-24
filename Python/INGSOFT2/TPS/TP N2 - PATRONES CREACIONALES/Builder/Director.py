from IFacturaBuilder import IFacturaBuilder

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> IFacturaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: IFacturaBuilder) -> None:
        self._builder = builder

    def buildFacturaElectronica(self, nombreEmisor, rfcEmisor, nombreReceptor,
    rfcReceptor, fechaEmisor, lugarEmisor, horaEmisor, tipoCfdi) -> None:
        self.builder.nombreEmisor(nombreEmisor)
        self.builder.rfcEmisor(rfcEmisor)
        self.builder.nombreReceptor(nombreReceptor)
        self.builder.rfcReceptor(rfcReceptor)
        self.builder.fechaEmisor(fechaEmisor)
        self.builder.lugarEmisor(lugarEmisor)
        self.builder.horaEmisor(horaEmisor)
        self.builder.tipoCfdi(tipoCfdi)
    
    def buildFacturaComercial(self, nombreEmisor, domicilioComercial, personaContacto, 
    numeroTelefono, dirCorreo) -> None:
        self.builder.nombreEmisor(nombreEmisor)
        self.builder.domicilioComercial(domicilioComercial)
        self.builder.personaContacto(personaContacto)
        self.builder.numeroTelefonico(numeroTelefono)
        self.builder.dirCorreoElectronico(dirCorreo)

