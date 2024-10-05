
# Semana 3: Recursión y Permutaciones

~~## Días 1-2:~~
~~Practica con "Subconjuntos de una Lista" y "Generar Permutaciones de un Array".~~

~~## Días 3-4:~~
~~Trabaja en "Suma de Rango sin bucles" y "Número Mágico".~~

## Día 5

Revisión y optimización de los ejercicios de la semana.

---

### Subconjuntos de una Lista

**Descripción:**  
Escribe una función que tome un array de números enteros únicos y devuelva todos los posibles subconjuntos (el conjunto potencia).

**Ejemplo:**

subconjuntos([1, 2, 3]);
// [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

---

### Generar Permutaciones de un Array

**Descripción:**  
Escribe una función que reciba un array de números y devuelva todas las permutaciones posibles del array.

**Ejemplo:**

permutaciones([1, 2, 3]);
// [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

---

### Suma de Rango sin bucles

**Descripción:**  
Escribe una función recursiva que reciba dos números `a` y `b` y devuelva la suma de todos los números entre `a` y `b` (inclusive). No uses bucles.

**Ejemplo:**

sumaRango(1, 5); // 15 (1 + 2 + 3 + 4 + 5)

---

### Número Mágico

**Descripción:**  
Dado un array de números, encuentra el "número mágico", que se define como el número que aparece más de `n/2` veces en el array, donde `n` es la longitud del array.

**Ejemplo:**

numeroMagico([3, 3, 4, 2, 3, 3, 5, 3]); // 3
