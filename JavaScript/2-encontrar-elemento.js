function encontrarElementoUnico (array) {
    let unico = 0

    for (let i = 0; i < array.length; i++) {
        unico ^= array[i]
    }
    return unico
}

//crear un array
let array = [1, 2, 3, 4, 5, 6, 5, 4,3,2,1]

//encontramos el elemento unico
let unico = encontrarElementoUnico(array)

console.log(unico)
    