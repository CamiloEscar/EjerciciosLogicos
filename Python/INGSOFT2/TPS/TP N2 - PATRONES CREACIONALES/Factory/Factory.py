from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"{product.operation()}\n"

        return result

def client_code(creator: Creator) -> None:

    print(f"Cliente: No se cual remito estoy creando pero lo creo\n"
          f"{creator.some_operation()}", end="")