// 1. Número Capicúa
// Descripción: Escribe una función que reciba un número y devuelva true si es un número capicúa (se lee igual de izquierda a derecha que de derecha a izquierda) y false si no lo es.
// Ejemplo:
// esCapicua(121); // true
// esCapicua(123); // false

// 2. Frecuencia de Palabras
// Descripción: Crea una función que tome una cadena de texto y devuelva un objeto donde las claves son palabras y los valores son la cantidad de veces que cada palabra aparece en la cadena.
// Ejemplo:
// contarPalabras("hola mundo hola");
// { hola: 2, mundo: 1 }

// 3. Sumar Dígitos
// Descripción: Escribe una función que reciba un número entero positivo y devuelva la suma de sus dígitos. Si el resultado es mayor que 9, repite el proceso hasta obtener un solo dígito.
// Ejemplo:
// sumarDigitos(456); // 6 (4 + 5 + 6 = 15 -> 1 + 5 = 6)


// 4. Verificar Anagramas
// Descripción: Crea una función que reciba dos cadenas y devuelva true si son anagramas (si tienen las mismas letras en diferente orden), y false en caso contrario. Ignora los espacios y no distingas entre mayúsculas y minúsculas.
// Ejemplo:
// esAnagrama("listen", "silent"); // true
// esAnagrama("hello", "world"); // false


// 5. Buscar Duplicados en un Array
// Descripción: Escribe una función que tome un array y devuelva true si contiene elementos duplicados y false si todos son únicos.
// Ejemplo:
// tieneDuplicados([1, 2, 3, 4, 5]); // false
// tieneDuplicados([1, 2, 3, 3, 4, 5]); // true


// 6. Invertir Palabras
// Descripción: Crea una función que reciba una cadena de texto y devuelva la misma cadena pero con cada palabra invertida, manteniendo el orden de las palabras.
// Ejemplo:
// invertirPalabras("Hola Mundo"); // "aloH odnuM"


// 7. Número Faltante en una Secuencia
// Descripción: Escribe una función que reciba un array con una secuencia de números consecutivos, donde falta un número, y devuelve el número faltante.
// Ejemplo:
// numeroFaltante([1, 2, 4, 5]); // 3


// 8. Ordenar Alfabéticamente sin Funciones Integradas
// Descripción: Crea una función que reciba una cadena y devuelva la cadena ordenada alfabéticamente sin utilizar funciones de ordenamiento integradas (sort).
// Ejemplo:
// ordenarAlfabeticamente("dcba"); // "abcd"


// 9. Paréntesis Balanceados
// Descripción: Escribe una función que determine si una cadena tiene los paréntesis balanceados. Los paréntesis están balanceados si cada ( tiene un ) correspondiente en el orden adecuado.
// Ejemplo:
// parBalanceados("(())"); // true
// parBalanceados("(()"); // false


// 10. Secuencia de Fibonacci
// Descripción: Crea una función que reciba un número n y devuelva el n-ésimo término de la secuencia de Fibonacci, sin utilizar recursión.
// Ejemplo:
// fibonacci(7); // 13


// 11. Movimiento en un Plano
// Descripción: Escribe una función que reciba un array de movimientos (por ejemplo, ["arriba", "abajo", "izquierda", "derecha"]) y determine si un objeto que comienza en el origen (0,0) regresa al punto de inicio después de realizar todos los movimientos. Cada movimiento afecta la posición de la siguiente manera:
// "arriba": incrementa y en 1.
// "abajo": decrementa y en 1.
// "izquierda": decrementa x en 1.
// "derecha": incrementa x en 1.
// Ejemplo:
// regresaAlInicio(["arriba", "abajo", "izquierda", "derecha"]); // true
// regresaAlInicio(["arriba", "izquierda", "abajo"]); // false


// 12. Par de Suma Objetivo
// Descripción: Dado un array de números enteros y un número objetivo, encuentra dos números en el array que sumen el objetivo y devuelve sus índices en un array. Si no hay ninguna combinación que sume el objetivo, devuelve un array vacío.
// Ejemplo:
// sumaObjetivo([2, 7, 11, 15], 9); // [0, 1] (ya que 2 + 7 = 9)


// 13. Comprimir Cadena
// Descripción: Escribe una función que reciba una cadena de caracteres y devuelva una versión comprimida de la cadena. La compresión consiste en reemplazar las secuencias consecutivas de caracteres por el carácter seguido del número de repeticiones. Si la cadena comprimida no es más corta que la original, devuelve la original.
// Ejemplo:
// comprimirCadena("aabcccccaaa"); // "a2b1c5a3"
// comprimirCadena("abc"); // "abc" (ya que no es más corta)


// 14. Contar Islas en una Cuadrícula
// Descripción: Dado un array bidimensional que representa un mapa de 1s (tierra) y 0s (agua), escribe una función que cuente cuántas islas hay. Una isla está formada por 1s conectados horizontal o verticalmente y está rodeada de agua.
// Ejemplo:
// contarIslas([
//   [1, 1, 0, 0, 0],
//   [1, 1, 0, 0, 1],
//   [0, 0, 0, 1, 1],
//   [0, 0, 0, 0, 0],
//   [1, 0, 1, 0, 1]
// ]); // 5


// 15. Eliminar Duplicados de una Lista Enlazada
// Descripción: Crea una función que elimine los nodos duplicados de una lista enlazada sin usar memoria adicional. Solo puedes modificar los punteros de los nodos.
// Ejemplo:
// Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
// Output: 1 -> 2 -> 3 -> 4 -> 5


// 16. Buscar el Primer Elemento Único
// Descripción: Escribe una función que reciba una cadena y devuelva el primer carácter único (no repetido) en ella. Si todos los caracteres se repiten, devuelve -1.
// Ejemplo:
// primerUnico("abracadabra"); // "c"
// primerUnico("aabb"); // -1


// 17. Rotación de una Matriz NxN
// Descripción: Dada una matriz cuadrada de n x n, rota la matriz 90 grados en el sentido de las agujas del reloj sin usar otra matriz. Hazlo en el lugar, modificando la matriz original.
// Ejemplo:
// Input:
// [[1, 2, 3],
//  [4, 5, 6],
//  [7, 8, 9]]
//
// Output:
// [[7, 4, 1],
//  [8, 5, 2],
//  [9, 6, 3]]


// 18. Subconjuntos de una Lista
// Descripción: Escribe una función que tome un array de números enteros únicos y devuelva todos los posibles subconjuntos (el conjunto potencia).
// Ejemplo:
// subconjuntos([1, 2, 3]);
// [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]


// 19. Suma de Rango sin bucles
// Descripción: Escribe una función recursiva que reciba dos números a y b y devuelva la suma de todos los números entre a y b (inclusive). No uses bucles.
// Ejemplo:
// sumaRango(1, 5); // 15 (1 + 2 + 3 + 4 + 5)


// 20. Árbol Binario de Búsqueda Válido
// Descripción: Dado un árbol binario, escribe una función para verificar si es un árbol de búsqueda binario (BST). Un BST es un árbol donde cada nodo sigue la propiedad de que su valor es mayor que los valores de su subárbol izquierdo y menor que los valores de su subárbol derecho.
// Ejemplo:
// esBST(root); // true o false dependiendo de la estructura del árbol