# 1. Generar un grafo con 15 vértices aleatorios no repetidos (con números de 1 a 100), luego agregar
# 30 aristas –no repetidas– que conecten vértices de manera aleatoria, con etiquetas –también
# aleatorias– dentro del rango de 1 a 100, después resolver las siguientes actividades:

import random as r


class Node:
    """represents a node containing 1 or 0 values in a binary tree."""

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

    def sort_val(self, val):
        """Inserts the selected value in the correct node"""

        if self.val is None:
            self.val = val

        elif val < self.val:
            if self.left is None:
                self.left = Node()
            self.left.sort_val(val)

        elif val > self.val:
            if self.right is None:
                self.right = Node()
            self.right.sort_val(val)

    def show_tree(self):
        """Shows the value of the selected node and all its childs sorted."""
        if self.left:
            self.left.show_tree()
        print(self.val)
        if self.right:
            self.right.show_tree()


num_list = [r.randint(1, 1000) for _ in range(100)]
print(num_list)

root = Node()
for num in num_list:
    root.sort_val(num)

root.show_tree()

# a. primero eliminar los vértices que hayan quedado desconectados, es decir, que ningún otro
# vértice tenga una arista que lo apunte y que de él no salga ninguna arista;

# b. determinar el nodo con mayor cantidad de aristas que salen de él, puede ser más de uno;

# c. determinar el nodo con mayor cantidad de aristas que llegan a él, puede ser más de uno;

# d. indicar los vértices desde los cuales no se puede acceder a otro vértice;

# e. contar cuantos vértice componen el grafo, dado que se genera aleatoriamente y se elimi-
# nan los vértices que quedan desconectados;

# f. determinar cuántos vértices tienen un arista a sí mismo, es decir, un ciclo directo;

# g. determinar la arista más larga, indicando su origen, destino y valor –puede ser más de una.