from unicodedata import name
from lista import Lista

# Necesito urgente un listado filtrado de los
# datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con
# nivel  ́critical’ o ‘high’. [actividad para resolver]

class dinosaurs:

    def __init__(self,nombre, type, numero, periodo, named_by):
        self.nombre = nombre
        self.type = type
        self.numero = numero
        self.periodo = periodo
        self.named_by = named_by

    def __str__(self):
        return f"{self.nombre} {self.type}, {self.numero},  {self.periodo},  {self.named_by}"



class nodoLista():
    info, sig, sublista = None, None, None



class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig

lista_dinosaurios = Lista()

for dinosaurs in dinosaurs:
        lista_dinosaurios.insertar(dinosaurs(type=['type'],
                                        name=['nombre'],
                                        numero=['numero'],
                                        periodo=['periodo'],
                                        named_by=['named_by'],))