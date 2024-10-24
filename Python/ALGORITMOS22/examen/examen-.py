from pila import Pila
from cola import Cola
from lista import Lista
from jurassic_park import dinosaurs

class nodoLista():
    info, sig, sublista = None, None, None
class Dinosaurios:

    def __init__(self,time, zone_code, dino_number, alert_level):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level= alert_level

    def __str__(self):
        return f"{self.time} | {self.zone_code} | {self.dino_number} | {self.alert_level}"


lista_jurasic = Lista()
lista_jurasic2 = Lista()
lista_jurasic3 = Lista()
lista_jurasic4 = Lista()

dinosaurs = [
    {'name': 'Tyrannosaurus Rex', 'type': 'carnívoro ', 'number': 8,
     'period': 'cretácico superior', 'named_by': 'Osborn, 1905'},
    {'name': 'Mosasaurus', 'type': 'carnívoro ', 'number': 11,
     'period': 'cretácico superior', 'named_by': 'Mantell, 1829'},
    {'name': 'Carnotaurus', 'type': 'carnívoro ', 'number': 14,
     'period': 'cretácico superior', 'named_by': 'Bonaparte, 1985'},
    {'name': 'Raptors (Dromaeosauridae)', 'type': 'carnívoro ', 'number': 4,
     'period': 'cretácico', 'named_by': 'Matthew & Brown, 1922'},
    {'name': 'Pteranodon', 'type': 'carnívoro ', 'number': 6,
     'period': 'cretácico superior', 'named_by': 'Marsh, 1876'},
    {'name': 'Compsognathus', 'type': 'carnívoro ', 'number': 2,
     'period': 'jurásico superior', 'named_by': 'Wagner, 1859'},
    {'name': 'Giganotosaurus', 'type': 'carnívoro ', 'number': 16,
     'period': 'cretácico superior', 'named_by': 'Coria & Salgado, 1995'},
    {'name': 'Allosaurus', 'type': 'carnívoro ', 'number': 15,
     'period': 'jurásico superior', 'named_by': 'Marsh, 1877'},
    {'name': 'Spinosaurus', 'type': 'carnívoro ', 'number': 13,
     'period': 'cretácico superior', 'named_by': 'Stromer, 1915'},
    {'name': 'Dilophosaurus', 'type': 'carnívoro ', 'number': 3,
     'period': 'jurásico inferior', 'named_by': 'Welles, 1954'},
    {'name': 'Triceratops', 'type': 'herbívoro ', 'number': 10,
     'period': 'cretácico superior', 'named_by': 'Marsh, 1889'},
    {'name': 'Brachiosaurus', 'type': 'herbívoro ', 'number': 12,
     'period': 'jurásico superior', 'named_by': 'Riggs, 1903'},
    {'name': 'Diplodocus', 'type': 'herbívoro ', 'number': 7,
     'period': 'jurásico superior', 'named_by': 'Marsh, 1878'},
    {'name': 'Stegosaurus', 'type': 'herbívoro ', 'number': 5,
     'period': 'jurásico superior', 'named_by': 'Marsh, 1887'},
    {'name': 'Parasaurolophus', 'type': 'herbívoro ', 'number': 9,
     'period': 'cretácico superior', 'named_by': 'Parks, 1922'},
    {'name': 'Ankylosaurus', 'type': 'herbívoro ', 'number': 1,
     'period': 'cretácico superior', 'named_by': 'Brown, 1908'},
    {'name': 'Pachycephalosaurus', 'type': 'herbívoro ', 'number': 17,
     'period': 'cretácico superior', 'named_by': 'Brown & Schlaikjer, 1943'},
]

file = open('alerts.txt')
lineas = file.readlines()

lista = []

for linea in lineas:
    datos = linea.split(';')
    print(datos)
    lista_jurasic.insertar(Dinosaurios(datos[0],
                                        datos[1],
                                        datos[2],
                                        datos[3]),

                                campo='time')

    lista_jurasic2.insertar(Dinosaurios(datos[0],
                                           datos[1],
                                           datos[2],
                                           datos[3]),
                                campo='zone_code')

    lista_jurasic3.insertar(Dinosaurios(datos[0],
                                        datos[1],
                                        datos[2],
                                        datos[3]),
                                campo='dino_number')

    lista_jurasic4.insertar(Dinosaurios(datos[0],
                                        datos[1],
                                        datos[2],
                                        datos[3]),
                                campo='alert_level')
    ista_jurasic = Lista()

for dino in dinosaurs:
    lista_jurasic.insertar(Dinosaurios(dino['number'],
                                     dino['name'].title(),
                                     dino['period'].capitalize(),
                                     dino['type'].capitalize(),
                                     dino['named_by'].title()), 'named_by')


dato = lista_jurasic.busqueda('Coria & Salgado, 1995'.title(), 'named_by')
if dato:
    print(f'el ultimo dinosaurio fue descubierto en {dato.info.named_by}')






def mostrar_elemento (lista, pos):
    dinos = lista.obtener_elemento(pos)
    print('• Nombre:', dinos['name'], ' | number:', dinos['number'], ' | period:', dinos['period'], ' | type(s):', dinos['type'])
    print (' named_by', dinos['named_by'])


print() 

#a. listado ordenado por nombre y por especie;
print('Listado ordenado por nombre:')
for i in range(lista_jurasic.tamanio()):
    mostrar_elemento(lista_jurasic, i)

print()


lista_jurasic.barrido()
lista_jurasic2.barrido()
print()
print(lista_jurasic2.tamanio())
print()
lista_jurasic3.barrido()
lista_jurasic4.barrido()
print()






lista_jurasic2.eliminar('WYG075', 'zone_code')
lista_jurasic2.eliminar('SXH966', 'zone_code')
lista_jurasic2.eliminar('LYF010', 'zone_code')
print(lista_jurasic2.tamanio())

dato = lista_jurasic.busqueda('carnivoro', 'type')
while(not lista_jurasic.lista_vacia()):
    
    if dato:
        print(dato)
        cola_carni = dato

def barrido_dino(self):
         for dinosaurs in self.__dinosaurs:
            print(dinosaurs['name'], dinosaurs['named_by'])
            print(barrido_dino)
