from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    contar_heroes_villanos,
    busqueda,
    preorden,
    postorden,
    por_nivel,
    altura,
    contar_pares_impares,
)

arb = nodoArbol()

# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

import random

# for i in range(10):
#     print(random.randrange(1, 9, 2))

# if __name__ == '__main__':

# 	start = 2   # inclusive
# 	end = 5	# exclusive

# 	n = 10  	# size

# 	x = [random.randrange(start, end) for _ in range(n)]
# 	print(x)

# for i in range(100):
#     print(random.randint(1, 100))
#arbol_numeros = arb(5)
insertar_nodo(arb, 1)
insertar_nodo(arb, 3)
insertar_nodo(arb, 2)
insertar_nodo(arb, 4)
insertar_nodo(arb, 5)
insertar_nodo(arb, 6)
insertar_nodo(arb, 7)
insertar_nodo(arb, 8)
insertar_nodo(arb, 9)
insertar_nodo(arb, 10)
insertar_nodo(arb, 11)
insertar_nodo(arb, 12)
insertar_nodo(arb, 13)
insertar_nodo(arb, 14)
insertar_nodo(arb, 15)

# insertar_nodo(arb, random.randint(1, 100))
#print(arb)
#A
#preorden(arb)
# print(arb)
# inorden(arb)
# postorden(arb)
# por_nivel(arb)

#B
# pos = busqueda(arb, 2)
# if pos:
#     print('asdasd', pos['info'])

#C
# value1 = eliminar_nodo(arb, 3)
# value2 = eliminar_nodo(arb, 4)
# value3 = eliminar_nodo(arb, 6)
# print('valor eliminado', value1,value2,value3)

#D
# altura(arb)
#print(arb)

#E
# pos = busqueda(arb, 1)
# print(arb)

#F 
# contar_pares_impares(arb)
# print(arb)


# 2. Implementar una función que permita cargar una expresión matemática en un árbol binario (no balanceado), y resuelva lo siguiente:

# a. determinar cuál de los barridos muestra la expresión en el orden correcto;
# b. resolver la expresión matemática y muestre el resultado.

# def  expresion_matematica (arbol):

# 3. Desarrollar un algoritmo que permita cargar el índice del libro Ingeniería de Software de Ian
# Summerville de manera automática desde un archivo de texto, transformando el árbol n-ario
# del índice en un árbol binario no balanceado mediante el uso de la transformada de Knuth,
# para resolver las siguientes actividades:

# a. listar el índice en su orden original;
# b. mostrar la parte del índice correspondiente al subtitulo “Diseño de software
# de tiempo real”;
# c. deberá almacenar además del texto de índice la página del libro donde está dicho tema;
# d. determinar cuántos capítulos tiene;
# e. determinar todos los temas que contengan las palabras modelo y métrica.



# 4. Implementar un algoritmo que contemple dos funciones, la primera que devuelva el hijo derecho de un nodo y la segunda que devuelva el hijo izquierdo.

# class NodoArbol:
#     def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
#         self.clave = clave
#         self.cargaUtil = valor
#         self.hijoIzquierdo = izquierdo
#         self.hijoDerecho = derecho
#         self.padre = padre

#     def tieneHijoIzquierdo(self):
#         return self.hijoIzquierdo

#     def tieneHijoDerecho(self):
#         return self.hijoDerecho

#     def esHijoIzquierdo(self):
#         return self.padre and self.padre.hijoIzquierdo == self

#     def esHijoDerecho(self):
#         return self.padre and self.padre.hijoDerecho == self

#     def esRaiz(self):
#         return not self.padre

#     def esHoja(self):
#         return not (self.hijoDerecho or self.hijoIzquierdo)

#     def tieneAlgunHijo(self):
#         return self.hijoDerecho or self.hijoIzquierdo

#     def tieneAmbosHijos(self):
#         return self.hijoDerecho and self.hijoIzquierdo

#     def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
#         self.clave = clave
#         self.cargaUtil = valor
#         self.hijoIzquierdo = hizq
#         self.hijoDerecho = hder
#         if self.tieneHijoIzquierdo():
#             self.hijoIzquierdo.padre = self
#         if self.tieneHijoDerecho():
#             self.hijoDerecho.padre = self


# class ArbolBinarioBusqueda:

#     def __init__(self):
#         self.raiz = None
#         self.tamano = 0

#     def longitud(self):
#         return self.tamano

#     def __len__(self):
#         return self.tamano

#     def agregar(self,clave,valor):
#         if self.raiz:
#             self._agregar(clave,valor,self.raiz)
#         else:
#             self.raiz = NodoArbol(clave,valor)
#         self.tamano = self.tamano + 1

#     def _agregar(self,clave,valor,nodoActual):
#         if clave < nodoActual.clave:
#             if nodoActual.tieneHijoIzquierdo():
#                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
#             else:
#                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
#         else:
#             if nodoActual.tieneHijoDerecho():
#                    self._agregar(clave,valor,nodoActual.hijoDerecho)
#             else:
#                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)

#     def __setitem__(self,c,v):
#        self.agregar(c,v)

#     def obtener(self,clave):
#        if self.raiz:
#            res = self._obtener(clave,self.raiz)
#            if res:
#                   return res.cargaUtil
#            else:
#                   return None
#        else:
#            return None

#     def _obtener(self,clave,nodoActual):
#        if not nodoActual:
#            return None
#        elif nodoActual.clave == clave:
#            return nodoActual
#        elif clave < nodoActual.clave:
#            return self._obtener(clave,nodoActual.hijoIzquierdo)
#        else:
#            return self._obtener(clave,nodoActual.hijoDerecho)

#     def __getitem__(self,clave):
#        return self.obtener(clave)

#     def __contains__(self,clave):
#        if self._obtener(clave,self.raiz):
#            return True
#        else:
#            return False

#     def eliminar(self,clave):
#       if self.tamano > 1:
#          nodoAEliminar = self._obtener(clave,self.raiz)
#          if nodoAEliminar:
#              self.remover(nodoAEliminar)
#              self.tamano = self.tamano-1
#          else:
#              raise KeyError('Error, la clave no está en el árbol')
#       elif self.tamano == 1 and self.raiz.clave == clave:
#          self.raiz = None
#          self.tamano = self.tamano - 1
#       else:
#          raise KeyError('Error, la clave no está en el árbol')

#     def __delitem__(self,clave):
#        self.eliminar(clave)

#     def empalmar(self):
#        if self.esHoja():
#            if self.esHijoIzquierdo():
#                   self.padre.hijoIzquierdo = None
#            else:
#                   self.padre.hijoDerecho = None
#        elif self.tieneAlgunHijo():
#            if self.tieneHijoIzquierdo():
#                   if self.esHijoIzquierdo():
#                      self.padre.hijoIzquierdo = self.hijoIzquierdo
#                   else:
#                      self.padre.hijoDerecho = self.hijoIzquierdo
#                   self.hijoIzquierdo.padre = self.padre
#            else:
#                   if self.esHijoIzquierdo():
#                      self.padre.hijoIzquierdo = self.hijoDerecho
#                   else:
#                      self.padre.hijoDerecho = self.hijoDerecho
#                   self.hijoDerecho.padre = self.padre

#     def encontrarSucesor(self):
#       suc = None
#       if self.tieneHijoDerecho():
#           suc = self.hijoDerecho.encontrarMin()
#       else:
#           if self.padre:
#                  if self.esHijoIzquierdo():
#                      suc = self.padre
#                  else:
#                      self.padre.hijoDerecho = None
#                      suc = self.padre.encontrarSucesor()
#                      self.padre.hijoDerecho = self
#       return suc

#     def encontrarMin(self):
#       actual = self
#       while actual.tieneHijoIzquierdo():
#           actual = actual.hijoIzquierdo
#       return actual

#     def remover(self,nodoActual):
#          if nodoActual.esHoja(): #hoja
#            if nodoActual == nodoActual.padre.hijoIzquierdo:
#                nodoActual.padre.hijoIzquierdo = None
#            else:
#                nodoActual.padre.hijoDerecho = None
#          elif nodoActual.tieneAmbosHijos(): #interior
#            suc = nodoActual.encontrarSucesor()
#            suc.empalmar()
#            nodoActual.clave = suc.clave
#            nodoActual.cargaUtil = suc.cargaUtil

#          else: # este nodo tiene un (1) hijo
#            if nodoActual.tieneHijoIzquierdo():
#              if nodoActual.esHijoIzquierdo():
#                  nodoActual.hijoIzquierdo.padre = nodoActual.padre
#                  nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
#              elif nodoActual.esHijoDerecho():
#                  nodoActual.hijoIzquierdo.padre = nodoActual.padre
#                  nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
#              else:
#                  nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
#                                     nodoActual.hijoIzquierdo.cargaUtil,
#                                     nodoActual.hijoIzquierdo.hijoIzquierdo,
#                                     nodoActual.hijoIzquierdo.hijoDerecho)
#            else:
#              if nodoActual.esHijoIzquierdo():
#                  nodoActual.hijoDerecho.padre = nodoActual.padre
#                  nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
#              elif nodoActual.esHijoDerecho():
#                  nodoActual.hijoDerecho.padre = nodoActual.padre
#                  nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
#              else:
#                  nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
#                                     nodoActual.hijoDerecho.cargaUtil,
#                                     nodoActual.hijoDerecho.hijoIzquierdo,
#                                     nodoActual.hijoDerecho.hijoDerecho)




# miArbol = ArbolBinarioBusqueda()
# miArbol[3]="rojo"
# miArbol[4]="azul"
# miArbol[6]="amarillo"
# miArbol[2]="en"

# print(miArbol[6])
# print(miArbol[2])

# def encontrarSucesor(self):
#     suc = None
#     if self.tieneHijoDerecho():
#         suc = self.hijoDerecho.encontrarMin()
#     else:
#         if self.padre:
#                if self.esHijoIzquierdo():
#                    suc = self.padre
#                else:
#                    self.padre.hijoDerecho = None
#                    suc = self.padre.encontrarSucesor()
#                    self.padre.hijoDerecho = self
#     return suc

# def encontrarMin(self):
#     actual = self
#     while actual.tieneHijoIzquierdo():
#         actual = actual.hijoIzquierdo
#     return actual

# def empalmar(self):
#     if self.esHoja():
#         if self.esHijoIzquierdo():
#                self.padre.hijoIzquierdo = None
#         else:
#                self.padre.hijoDerecho = None
#     elif self.tieneAlgunHijo():
#         if self.tieneHijoIzquierdo():
#                if self.esHijoIzquierdo():
#                   self.padre.hijoIzquierdo = self.hijoIzquierdo
#                else:
#                   self.padre.hijoDerecho = self.hijoIzquierdo
#                self.hijoIzquierdo.padre = self.padre
#         else:
#                if self.esHijoIzquierdo():
#                   self.padre.hijoIzquierdo = self.hijoDerecho
#                else:
#                   self.padre.hijoDerecho = self.hijoDerecho
#                self.hijoDerecho.padre = self.padre

