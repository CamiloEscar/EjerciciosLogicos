// // Función para invertir un array
// function invertirArray(array) {
//     let arrayInvertido = new Array(array.length);

//     for (let i = 0; i < array.length; i++) {
//       arrayInvertido[array.length - 1 - i] = array[i];
//     }

//     return arrayInvertido;
//   }

//   // Función para manipular el array: invertirlo, pushear un valor y eliminar un elemento
//   function manipularArray(array, valorPush) {
//     // Invertir el array
//     let arregloInvertido = invertirArray(array);

//     // Mostrar el array invertido sin modificar el original
//     console.log('Array invertido:', arregloInvertido);

//     // Pushear el valor
//     arregloInvertido.push(valorPush);

//     // Eliminar el elemento (índice 2) si existe
//     if (arregloInvertido.length > 2) {
//       console.log('Elemento eliminado:', arregloInvertido.splice(2, 1));
//     }

//     return arregloInvertido;
//   }

//   // Función para añadir un nuevo valor al array
//   function anadirValor(array, nuevoValor) {
//     array.push(nuevoValor);
//   }

//   // Ejemplo de uso
//   let arrayOriginal = [1, 2, 3, 4, 5];

//   // Mostrar el array original
//   console.log('Array original:', arrayOriginal);

//   // Manipular el array
//   let arrayManipulado = manipularArray(arrayOriginal, 'nuevo valor');

//   // Imprimir el array manipulado
//   console.log('Array manipulado:', arrayManipulado);

//   // Añadir un nuevo valor en otra función
//   anadirValor(arrayManipulado, 'nuevo valor 2');

//   // Imprimir el array después de añadir el nuevo valor
//   console.log('Array después de añadir valor:', arrayManipulado);

//funcion para invertir un array sin usar metodos
function invertirArray(array) {
  let arrayInvertido = new Array(array.length);

  for (let i = array.length - 1; i >= 0; i--) {
    arrayInvertido[array.length - i - 1] = array[i];
  }

  return arrayInvertido;
}

//funcion para agregar un valor al final del array
function agregarValor(array, valor) {
  let nuevoArray = new Array(array.length + 1);
  for (let i = 0; i < array.length; i++) {
    nuevoArray[i] = array[i];
  }
  nuevoArray[nuevoArray.length - 1] = valor;

  return nuevoArray;
}

//funcion para eliminar un valor de un indice especidifo del array
function eliminarValor(array, indice) {
  if (indice >= array.length) return array;

  let nuevoArray = new Array(array.length - 1);
  for (let i = 0; i < indice; i++) {
    nuevoArray[i] = array[i];
  }

  for (let i = indice; i < nuevoArray.length; i++) {
    nuevoArray[i] = array[i + 1];
  }

  return nuevoArray;
}

//funcion que llama a las variables para manipularlo
function manipularArray(array, valorAgregar) {
  //invertir el array
  let arregloInvertido = invertirArray(array);

  //agregar un valor al final
  let arregloConValorAgregado = agregarValor(arregloInvertido, valorAgregar);

  //eliminamos el elemento del indice 2
  let arregloFinal = eliminarValor(arregloConValorAgregado, 2);

  return arregloFinal;
}

//usos
let arrayOriginal = [1, 2, 3, 4, 5];

//mostrar el array original
console.log("array original: ", arrayOriginal);

console.log("array invertido: ", invertirArray(arrayOriginal));

//manipular array
let arrayManipulado = manipularArray(arrayOriginal, "nuevo valor");

console.log("array manipulado: ", arrayManipulado);

//añadir un nuevo valor al final de la otra funcion
arrayManipulado = agregarValor(arrayManipulado, "nuevo valor 2");

console.log("array despues de añadir el otro valor 2: ", arrayManipulado);
