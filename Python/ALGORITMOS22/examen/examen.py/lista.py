
def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoLista():
    info, sig, sublista = None, None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig
    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_anterior_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.aparicion < 1963):
                print(aux.info)
            aux = aux.sig
    
    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    def barrido_porcentaje_victorias(self):
        aux = self.__inicio
        while(aux is not None):
            total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            if(aux.info.batallas_ganadas / total >= 0.79):
                print(aux.info)
            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1 

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    def contar_por_casa(self):
        marvel, dc = 0, 0

        aux = self.__inicio
        while(aux is not None):
            if(aux.info.casa.capitalize() == 'Marvel'):
                marvel += 1
            if(aux.info.casa.capitalize() == 'Dc'):
                dc += 1
            aux = aux.sig

        return marvel, dc
    
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                break
            aux = aux.sig
        return mayor

# cadena = 'hola'
# cadena.startswith('C')
# print(cadena[0])

# class Persona:

#     def __init__(self, apellido, nombre, dni):
#         self.apellido = apellido
#         self.nombre = nombre
#         self.dni = dni
#         self.telefono = None
    
#     def __str__(self):
#         return f"{self.apellido} {self.nombre}, {self.dni}"



# p = Persona('A', 'A', 3)
# num = 45
# cadena = 'hola'
# print(criterio(p, 'mail'))
# print(criterio(p, 'apellido'))
# print(criterio(num))
# print(criterio(num, 'tel'))
# print(criterio(cadena, 'mail'))
# print(criterio(cadena))


# l = Lista()

# l.insertar(Persona('A', 'A', 7), 'nombre')
# l.insertar(Persona('C', 'C', 2), 'nombre')
# l.insertar(Persona('A', 'A', 11), 'nombre')
# l.insertar(Persona('B', 'Z', 1), 'nombre')
# l.insertar(Persona('B', 'H', 10), 'nombre')
# l.insertar(Persona('B', 'X', 4), 'nombre')

# Persona dni = 5 nombre = G




# l.eliminar('A', 'nombre')
# l.insertar(11)
# l.insertar(8)
# l.insertar(9)
# l.insertar(10)
# l.insertar(5)

# print(l.obtener_elemento(0))
# print(l.obtener_elemento(-2))
# print(l.obtener_elemento(5))
# print(l.obtener_elemento(8))

# pos = l.eliminar(8)
# if pos is not None:
#     l.insertar(18)


# print(l.eliminar(5))
# print(l.eliminar(7))
# print(l.eliminar(10))


# l.barrido()

# print(l.busqueda(7).info)
# print(l.busqueda(2))


# vocales = ['A', 'E',.....]

# for vocal in vocale:
#     aux = l.eliminar(vocal)
#     while(aux is not None):
#         aux = l.eliminar(vocal)

# class Weather():

#     def __init__(self, id, temp, hum, pres):
#         self.id = id
#         self.temp = temp
#         self.hum = hum
#         self.pres = pres

#     def __str__(self):
#         return f'{self.id} - {self.temp} - {self.hum} - {self.pres}'


# lista_estaciones = Lista()

# lista_estaciones.insertar('A')
# lista_estaciones.insertar('G')
# lista_estaciones.insertar('L')
# lista_estaciones.insertar('O')
# lista_estaciones.insertar('Y')


# # lista_estaciones.barrido()

# clima = Weather(24, 15, 80, 1004)
# clima2 = Weather(12, 20, 80, 1024)
# estacion = lista_estaciones.busqueda('L')
# estacion.sublista.insertar(clima, 'id')
# estacion.sublista.insertar(clima2, 'id')

# lista_estaciones.barrido_lista_lista()

# clima_buscado = estacion.sublista.busqueda(12, 'id')
# if(clima_buscado):
#     clima_buscado.info.hum = 90

# print()
# lista_estaciones.barrido_lista_lista()





def __criterio(dato, criterio):
    if(criterio is None):
        return dato
    else:
        return dato[criterio]

def quicksort(vector, inicio, fin, criterio=None):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(__criterio(vector[primero], criterio) <= __criterio(vector[pivote], criterio) and primero <= ultimo):
            primero += 1
        while(__criterio(vector[ultimo], criterio) > __criterio(vector[pivote], criterio) and ultimo >= primero):
            ultimo -= 1
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(__criterio(vector[pivote], criterio) < __criterio(vector[primero], criterio)):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1, criterio)
    if(fin > primero):
        quicksort(vector, primero + 1, fin, criterio)

class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos = []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]

    def insertar(self, dato, criterio=None): #! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato) 

    def insertarPos(self,pos,dato):
        self.__elementos.insert(pos, dato)

    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None

    def eliminarPos(self,pos):
        return self.__elementos.pop(pos)

    def modificar_elemento(self, pos, nuevo_valor, criterio=None):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor, criterio)

    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1
        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1
        return pos
    
    def obtener_elemento(self, pos):
        if(pos >= 0):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)
    
    def barrido_jedi(self):
        for elemento in self.__elementos:
            print(elemento['name'], elemento['especie'])
    
    def barrido_stormtrooper(self, numero):
        for elemento in self.__elementos:
            if(elemento['codigo'] % 1000 == numero):
                print(elemento['legion'], elemento['codigo'])
    
    def barrido_stormtrooper_legion(self, legion):
        for elemento in self.__elementos:
            if(elemento['legion'] == legion):
                print(elemento['legion'], elemento['codigo'])
    
    def barrido_green(self):
        for elemento in self.__elementos:
            if('green' in elemento['lightsaber_color']):
                print(elemento['name'])
    
    def barrido_lista_autos(self):
        for elemento in self.__elementos:
            print(elemento)
            print('autos:')
            elemento['autos'].barrido()

    def barrido_eliminando(self, datos_eliminar):
        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)
    
    def ordenar(self, criterio=None):
        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)