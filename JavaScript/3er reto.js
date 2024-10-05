/*
En el taller de Santa, un elfo travieso ha estado jugando en la cadena de fabricación de regalos, añadiendo o eliminando un paso no planificado.

Tienes la secuencia original de pasos en la fabricación original y la secuencia modificada modified que puede incluir un paso extra o faltar un paso.

Tu tarea es escribir una función que identifique y devuelva el primer paso extra que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia entre las secuencias, devuelve una cadena vacía.

const original = 'abcd'
const modified = 'abcde'
findNaughtyStep(original, modified) // 'e'

const original = 'stepfor'
const modified = 'stepor'
findNaughtyStep(original, modified) // 'f'

const original = 'abcde'
const modified = 'abcde'
findNaughtyStep(original, modified) // ''
A tener en cuenta:

Siempre habrá un paso de diferencia o ninguno.
La modificación puede ocurrir en cualquier lugar de la cadena.
La secuencia original puede estar vacía
*/

function findNaughtyStep(original, modified) {
    if (original.length === modified.length) return "" 
    
    //const count = Math.max(original.length, modified.length)
    const iterator = modified.length > original.length ? modified : original

    //for (let index = 0; index < count; index++) {
    for (let index = 0; index < iterator.length; index++) {    
        if (original[index] !== modified [index]) {
          return iterator[index]
            //return modified.length > original.length ? modified[index] : original[index]
        }
      }
    }

// Definición de la función findNaughtyStep que toma dos cadenas de texto como argumentos: original y modified.
function findNaughtyStep(original, modified) {
    // Verificar si las longitudes de ambas cadenas son iguales. Si es así, no hay caracteres diferentes.
    // En este caso, la función devuelve una cadena vacía.
    if (original.length === modified.length) return "";
  
    // Calcular el número máximo entre las longitudes de original y modified.
    const count = Math.max(original.length, modified.length);

    // Iterar a través de los índices hasta el número máximo de caracteres.
    for (let index = 0; index < count; index++) {
        // Verificar si el carácter en el índice actual es diferente en ambas cadenas.
        if (original[index] !== modified[index]) {
            // Si la longitud de modified es mayor que la longitud de original,
            // devolver el carácter en ese índice en modified. De lo contrario, devolver el carácter en original.
            return modified.length > original.length ? modified[index] : original[index];
        }
    }
}

// obtener el numero de caracteres de la cadena mas larga
//itero cada caracter y chequeo si el indice actual del original es igual al del modificado
// si sobra un caracter devuelvo el modificado
// si falta un caracter devuelvo el del original