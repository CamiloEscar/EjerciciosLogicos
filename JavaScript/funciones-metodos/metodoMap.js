// La funcion del metodo .map() en javascript, crea un nuevo arreglo aplicandouna funcion de cada elemento del arreglo original, en este caso para encontrar el exponente al cuadrado de cada numero se utiliza el metodo .map()

const numeros = [1, 2, 3, 4, 5, 6];
const cuadrado = numeros.map((numero) => {
  return numero * numero;
});

console.log(cuadrado)