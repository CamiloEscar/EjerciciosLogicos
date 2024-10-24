from Director import Director
from ConcreteFacturaBuilder import ConcreteFacturaBuilder
from IFacturaBuilder import IFacturaBuilder

director = Director()
facturaBuilder = ConcreteFacturaBuilder()

director.builder = facturaBuilder

print("Factura electronica")
director.buildFacturaElectronica('Gonzalo', '123', 'Emi', '1245', '17/03/05',
'25 de mayo 168', '17:30', 'A')
facturaBuilder.factura.listar_partes()

print('\n\nFactura Comercial')
director.buildFacturaComercial('Gonzalo', '25 de mayo 123', 'Clara', '3446507537', 'errandoneagonzalo18@gmail.com')
facturaBuilder.factura.listar_partes()