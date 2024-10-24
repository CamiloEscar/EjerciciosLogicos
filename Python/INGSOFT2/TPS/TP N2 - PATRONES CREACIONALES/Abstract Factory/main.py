from ConcreteFactoryMonitor import ConcreteFactoryMonitor
from ConcreteFactoryMouse import ConcreteFactoryMouse
from ConcreteFactoryTeclado import ConcreteFactoryTeclado

from client_code import client_code, client_code_2

print("Client: Testeando client code con el primer tipo de factory:")
client_code(ConcreteFactoryMonitor(), 
            ConcreteFactoryMouse(), 
            ConcreteFactoryTeclado())


print("\n")

print("Client: Testeando client code con el segundo tipo de factory:")
client_code_2(ConcreteFactoryMonitor(), 
            ConcreteFactoryMouse(), 
            ConcreteFactoryTeclado())