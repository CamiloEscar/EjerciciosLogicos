# Semana 4: Simulación de Entrevista

Días 1-3: Selecciona problemas de semanas anteriores y resuélvelos en un tiempo determinado (30-45 minutos por problema) para simular condiciones de entrevista.
Día 4: Revisa soluciones para optimizar el rendimiento y la claridad del código.
Día 5: Repasa cualquier área donde sientas que necesitas más práctica y asegúrate de comprender cada tipo de problema.

***Ejercicios de Lógica y Programación***

Estos problemas están diseñados para evaluar tu capacidad de razonamiento, manejo de estructuras de datos y habilidad para optimizar soluciones.

1. **Movimiento en un Plano**  
   **Descripción:** Escribe una función que reciba un array de movimientos (por ejemplo, ["arriba", "abajo", "izquierda", "derecha"]) y determine si un objeto que comienza en el origen (0,0) regresa al punto de inicio después de realizar todos los movimientos.  
   **Ejemplo:**

   ```javascript
   regresaAlInicio(["arriba", "abajo", "izquierda", "derecha"]); // true
   regresaAlInicio(["arriba", "izquierda", "abajo"]); // false
   ```

2. **Par de Suma Objetivo**  
   **Descripción:** Dado un array de números enteros y un número objetivo, encuentra dos números en el array que sumen el objetivo y devuelve sus índices en un array. Si no hay ninguna combinación que sume el objetivo, devuelve un array vacío.  
   **Ejemplo:**

   ```javascript
   sumaObjetivo([2, 7, 11, 15], 9); // [0, 1]
   ```

3. **Comprimir Cadena**  
   **Descripción:** Escribe una función que reciba una cadena de caracteres y devuelva una versión comprimida de la cadena. La compresión consiste en reemplazar las secuencias consecutivas de caracteres por el carácter seguido del número de repeticiones.  
   **Ejemplo:**

   ```javascript
   comprimirCadena("aabcccccaaa"); // "a2b1c5a3"
   comprimirCadena("abc"); // "abc"
   ```

4. **Contar Islas en una Cuadrícula**  
   **Descripción:** Dado un array bidimensional que representa un mapa de 1s (tierra) y 0s (agua), escribe una función que cuente cuántas islas hay. Una isla está formada por 1s conectados horizontal o verticalmente y está rodeada de agua.  
   **Ejemplo:**

   ```javascript
   contarIslas([
     [1, 1, 0, 0, 0],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1]
   ]); // 5
   ```

5. **Eliminar Duplicados de una Lista Enlazada**  
   **Descripción:** Crea una función que elimine los nodos duplicados de una lista enlazada sin usar memoria adicional. Solo puedes modificar los punteros de los nodos.  
   **Ejemplo:**

   ```javascript
   // Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
   // Output: 1 -> 2 -> 3 -> 4 -> 5
   ```

6. **Buscar el Primer Elemento Único**  
   **Descripción:** Escribe una función que reciba una cadena y devuelva el primer carácter único (no repetido) en ella. Si todos los caracteres se repiten, devuelve -1.  
   **Ejemplo:**

   ```javascript
   primerUnico("abracadabra"); // "c"
   primerUnico("aabb"); // -1
   ```

7. **Rotación de una Matriz NxN**  
   **Descripción:** Dada una matriz cuadrada de n x n, rota la matriz 90 grados en el sentido de las agujas del reloj sin usar otra matriz. Hazlo en el lugar, modificando la matriz original.  
   **Ejemplo:**

   ```javascript
   // Input:
   // [[1, 2, 3],
   //  [4, 5, 6],
   //  [7, 8, 9]]
   //
   // Output:
   // [[7, 4, 1],
   //  [8, 5, 2],
   //  [9, 6, 3]]
   ```

8. **Subconjuntos de una Lista**  
   **Descripción:** Escribe una función que tome un array de números enteros únicos y devuelva todos los posibles subconjuntos (el conjunto potencia).  
   **Ejemplo:**

   ```javascript
   subconjuntos([1, 2, 3]);
   // [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
   ```

9. **Suma de Rango sin bucles**  
   **Descripción:** Escribe una función recursiva que reciba dos números a y b y devuelva la suma de todos los números entre a y b (inclusive). No uses bucles.  
   **Ejemplo:**

   ```javascript
   sumaRango(1, 5); // 15
   ```

10. **Árbol Binario de Búsqueda Válido**  
    **Descripción:** Dado un árbol binario, escribe una función para verificar si es un árbol de búsqueda binario (BST).  
    **Ejemplo:**

    ```javascript
    esBST(root); // true o false dependiendo de la estructura del árbol
    ```
