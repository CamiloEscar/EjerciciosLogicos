//funcion para revertir cadena
function revertirCadena(texto) {
    let arregloTexto = texto.split("")

    let arregloInvertido = arregloTexto.reverse()
    let textoInvertido = arregloInvertido.join("")
    return textoInvertido
}

console.log(revertirCadena("hola"))

// https://www.instagram.com/p/C-LCuvgAXOI/