from typing import Any

class Factura():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def listar_partes(self) -> None:
        print(f"Partes de la factura: {', '.join(self.parts)}", end="")