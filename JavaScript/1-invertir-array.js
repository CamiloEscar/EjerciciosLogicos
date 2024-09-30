function invertirArray(array) {
  let resultado = new Array(array.length);

  for (let i = 0; i < array.length; i++) {
    resultado[array.length - 1 - i] = array[i];
  }

  return resultado;
}

let array = [1,2,3,4,5]

let arrayInvertido = invertirArray(array)

console.log(array)
console.log(arrayInvertido)