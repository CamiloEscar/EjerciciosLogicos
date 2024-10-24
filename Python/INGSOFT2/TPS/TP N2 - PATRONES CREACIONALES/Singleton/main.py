#Obtener el CUIT de la empresa.

from SingletonPersonal import SingletonPersonal
from SingletonVideoDigital import SingletonVideoDigital


empresaPersonal = SingletonPersonal()
empresaPersonal2 = SingletonPersonal()

empresaVideoDigital = SingletonVideoDigital()
empresaVideoDigital2 = SingletonVideoDigital()

print('Singleton Personal')
print(empresaPersonal is empresaPersonal2)

print('Singleton Video Digital')
print(empresaVideoDigital is empresaVideoDigital2)

print()
print('CUIT de ', empresaPersonal.getid(), ': ', empresaPersonal.getCuit())
print()
print('CUIT de ', empresaVideoDigital.getid(), ': ', empresaVideoDigital.getCuit())
