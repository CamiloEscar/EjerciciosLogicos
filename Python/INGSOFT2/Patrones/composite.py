#*--------------------------------------------------
#* composite.py
#* excerpt from https://refactoring.guru/design-patterns/composite/python/example
#*--------------------------------------------------

from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    La abstracción define la interfaz para la parte de "control" de los dos
    jerarquías de clases. Mantiene una referencia a un objeto del
    Jerarquía de implementación y delega todo el trabajo real a este objeto. La abstracción define la interfaz para la parte de "control" de los dos
    jerarquías de clases. Mantiene una referencia a un objeto del
    Jerarquía de implementación y delega todo el trabajo real a este objeto.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstracción: Operación base con:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    Puede extender la Abstracción sin cambiar las clases de Implementación.
    """

    def operation(self) -> str:
        return (f"Abstracción extendida: Operación extendida con:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    """
    La implementación define la interfaz para todas las clases de implementación. Eso
    no tiene que coincidir con la interfaz de Abstraction. De hecho, los dos
    Las interfaces pueden ser completamente diferentes. Por lo general, la interfaz de implementación
    proporciona sólo operaciones primitivas, mientras que la Abstracción define
    operaciones de nivel basadas en esas primitivas.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Cada Implementación Concreta corresponde a una plataforma específica e implementa
la interfaz de implementación utilizando la API de esa plataforma.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Aquí está el resultado en la plataforma A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "Implementación concreta: aquí está el resultado en la plataforma B."


def client_code(abstraction: Abstraction) -> None:
    """
    Excepto por la fase de inicialización, donde un objeto de Abstracción se vincula
    con un objeto de implementación específico, el código del cliente solo debe depender de
    la clase de Abstracción. De esta manera, el código del cliente puede admitir cualquier abstracción.
    combinación de implementación.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    El código del cliente debería poder trabajar con cualquier abstracción preconfigurada.
    combinación de implementación.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

    print("\n")
