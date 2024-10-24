// .reduce() en JavaScript se utiliza para reducir los elementos de un array a un solo valor. La operación que se realiza durante la reducción puede ser cualquier operación que combine dos elementos y devuelva un valor único, como la suma, resta, multiplicación, concatenación, etc.

const numeros = [1, 2, 3, 4, 5, 6];

const reducir = numeros.reduce(
  (acumulador, elementoActual) => acumulador + elementoActual
);

console.log(reducir)