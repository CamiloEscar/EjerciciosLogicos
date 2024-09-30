// metodo .filter() crea un nuevo arreglo con elementos que cumple una funcion especifica, en este ejemplo para encontrar cuales son los numeros pares se utiliza el numero filter.

const numeros = [1, 2, 3, 4, 5, 6];

const numeroPar = numeros.filter((numero) => numero % 2 === 0);

console.log(numeroPar)