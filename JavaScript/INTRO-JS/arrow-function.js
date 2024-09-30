
// function expression
let viajando = function(destino) {
    return `Viajando a la ciudad de  ${destino}`

}

let viaje = viajando('Paris')
console.log(viaje)

// Arrow Functions
let viajando2 = (destino, duracion) => {
 retunr  `Viajando a la ciudad de ${destino} por ${duracion}`

}

let viaje2 = viajando2('Londres', '9 dias')