import string
import utilidades

class Aplicacion:
    def request(self) -> str:
        return 'mensaje aplicacion'


class Servidor:
    def specific_request(self) -> str:
        mensaje = 'Mensaje del servidor'
        msj = utilidades.texto_a_binario(mensaje)[::-1]
        return msj


class AdaptadorTCP(Aplicacion, Servidor):
    def request(self) -> str:
        msj = self.specific_request()[::-1]
        msj_desencriptado = utilidades.binario_a_texto(msj)
        return msj_desencriptado


def client_code(target: Aplicacion) -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    app = Aplicacion()
    client_code(app)
    print("\n")

    servidor = Servidor()
    print(f"Adaptee: {servidor.specific_request()}", end="\n\n")
    
    adaptadorTcp = AdaptadorTCP()
    client_code(adaptadorTcp)
