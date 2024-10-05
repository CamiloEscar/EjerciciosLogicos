
# Semana 2: Problemas de Matrices y Lógica Condicional

## Días 1-2

Trabaja en **"Contar Islas en una Cuadrícula"** y **"Máximo Rectángulo en una Matriz de 1s"**.

### 1. Contar Islas en una Cuadrícula

**Descripción:** Dado un array bidimensional que representa un mapa de 1s (tierra) y 0s (agua), escribe una función que cuente cuántas islas hay. Una isla está formada por 1s conectados horizontal o verticalmente y está rodeada de agua.

**Ejemplo:**

`contarIslas([
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1]
]);` // 5

### 2. Máximo Rectángulo en una Matriz de 1s

**Descripción:** Dado un array bidimensional que contiene 1s y 0s, encuentra el área máxima de un rectángulo compuesto únicamente por 1s.

**Ejemplo:**

maxRectangulo([
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]); // 6

## Días 3-4

Practica **"Rotación de una Matriz NxN"** y **"Movimiento en un Plano"**.

### 3. Rotación de una Matriz NxN

**Descripción:** Dada una matriz cuadrada de n x n, rota la matriz 90 grados en el sentido de las agujas del reloj sin usar otra matriz. Hazlo en el lugar, modificando la matriz original.

**Ejemplo:**

// Input:
// [[1, 2, 3],
//  [4, 5, 6],
//  [7, 8, 9]]
//
// Output:
// [[7, 4, 1],
//  [8, 5, 2],
//  [9, 6, 3]]

### 4. Movimiento en un Plano

**Descripción:** Escribe una función que reciba un array de movimientos (por ejemplo, ["arriba", "abajo", "izquierda", "derecha"]) y determine si un objeto que comienza en el origen (0,0) regresa al punto de inicio después de realizar todos los movimientos. Cada movimiento afecta la posición de la siguiente manera:

- "arriba": incrementa y en 1.
- "abajo": decrementa y en 1.
- "izquierda": decrementa x en 1.
- "derecha": incrementa x en 1.

**Ejemplo:**

`regresaAlInicio(["arriba", "abajo", "izquierda", "derecha"]); // true`
`regresaAlInicio(["arriba", "izquierda", "abajo"]); // false`

## Día 5

Revisión de los ejercicios de la semana y mejora de soluciones.
