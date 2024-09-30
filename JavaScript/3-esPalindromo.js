function esPalindromo (array) {
    let inicio = 0
    let fin = array.length -1

    while (inicio < fin) {
        if (array[inicio] !== array[fin]) {
            return false
        }
        inicio++
        fin --
    }

    return true
}

let array1 = [1,2,3,2,1]
let array2 = [1,2,3,4,5]

//verificamos si los array son palindromos
console.log(esPalindromo(array1)) // true
console.log(esPalindromo(array2)) // false
