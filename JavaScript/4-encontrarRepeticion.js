function encontrarRepetido(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = i +1; j < array.length; j++) {
            if (array[i] === array[j]) {
                return array[i];
            }
        }
    }
    return null
}

let array1 = [1,2,3,4,5,6,6,7]
let array2 = [1,3,5,5,6,7,2]

console.log(encontrarRepetido(array1))
console.log(encontrarRepetido(array2))