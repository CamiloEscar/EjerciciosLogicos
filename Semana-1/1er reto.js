/*En la fábrica de juguetes del Polo Norte, cada juguete tiene un número de identificación único.

Sin embargo, debido a un error en la máquina de juguetes, algunos números se han asignado a más de un juguete.

¡Encuentra el primer número de identificación que se ha repetido, donde la segunda ocurrencia tenga el índice más pequeño!

En otras palabras, si hay más de un número repetido, debes devolver el número cuya segunda ocurrencia aparezca primero en la lista. Si no hay números repetidos, devuelve -1.

const giftIds = [2, 1, 3, 5, 3, 2]
const firstRepeatedId = findFirstRepeated(giftIds)
console.log(firstRepeatedId) // 3
// Aunque el 2 y el 3 se repiten
// el 3 aparece primero por segunda vez

const giftIds2 = [1, 2, 3, 4]
const firstRepeatedId2 = findFirstRepeated(giftIds2)
console.log(firstRepeatedId2) // -1
// Es -1 ya que no se repite ningún número

const giftIds3 = [5, 1, 5, 1]
const firstRepeatedId3 = findFirstRepeated(giftIds3)
console.log(firstRepeatedId3) // 5
*/

// Definición de la función findFirstRepeated que toma un array de regalos como argumento.
function findFirstRepeated(gifts) {
    // Crear un array vacío llamado 'mapa' para realizar un seguimiento de los elementos ya vistos.
    const mapa = []

    // Iterar a través de cada elemento (numero) en el array de regalos.
    for (const numero of gifts) {
        // Verificar si el elemento ya está en el 'mapa'.
        if (mapa.includes(numero)) {
            // Si el elemento ya está en el 'mapa', significa que es el primer elemento repetido.
            // En este caso, la función devuelve ese elemento repetido.
            return numero
        }
        
        // Si el elemento no está en el 'mapa', se agrega al 'mapa'.
        mapa.push(numero)
    }
    
    // Si no se encuentra ningún elemento repetido, la función devuelve -1.
    return -1
}
