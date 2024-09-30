// método .sort() Ordena los elementos de un arreglo según una función de comparación 

const numeros = [4, 5,6,1,3]

const ordenar = numeros.sort(
    (a,b) => a - b
)

console.log(ordenar)

