from TarjetaCredito import TarjetaCredito
from TarjetaDebito import TarjetaDebito
from VipCredito import VipCredito
from VipDebito import VipDebito

monto = 1000
#Tarjeta de credito y debito base
tCredito = TarjetaCredito()
tDebito = TarjetaDebito()

print('Tarjeta de credito\n')
print('Impuesto por ingreso de dinero: ' , tCredito.getimpuesto(), '$')
print('Puede pagar en cuotas?: ' , tCredito.puedePagarEnCuotas())
print('monto ingresado ', monto, '$ se ingresaran ', tCredito.ingresarDinero(monto), '$')

print('Tarjeta de debito\n')
print('Impuesto por ingreso de dinero: ' , tDebito.getimpuesto(), '$')
print('Puede pagar en cuotas?: ' , tDebito.puedePagarEnCuotas())
print('monto ingresado ', monto, '$ se ingresaran ', tDebito.ingresarDinero(monto), '$')

#Se agrega el VIP a la tarjeta de credito
print("\n\nTarjeta de credito con VIP\n")
tCreditoVIP = VipCredito(TarjetaCredito)
print('monto ingresado ', monto, '$ se ingresaran ', tCreditoVIP.ingresarDinero(monto), '$')

#Se agrega el VIP a la tarjeta de debito
tDebitoVIP = VipDebito(TarjetaDebito)
print("\nTarjeta de debito con VIP\n")
print('monto ingresado ', monto, '$ se ingresaran ', tDebitoVIP.ingresarDinero(monto), '$')
print('Puede pagar en cuotas?: ' , tDebitoVIP.puedePagarEnCuotas())