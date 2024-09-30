function encontrarFaltaNumero(array) {
    let n = array.length + 1
    let orden = (n * (n +1)) /2
    let sumaActual = array.reduce((acc, num) => acc + num, 0)

    return orden - sumaActual 
}

let array1 = [1,2,3,4,6]
console.log(encontrarFaltaNumero(array1)) 