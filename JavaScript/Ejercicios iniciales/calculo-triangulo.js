// Área triángulo
let base = 5
let height = 7

const areaTriangle = (base, height) => base * height / 2

console.log(`El área de un triángulo de base ${base} y height ${height} es: ${areaTriangle(base, height)}.`)

// Área rectángulo
// let width = 12
// let height = 6

// const areaSquare = (width, height) => width * height

console.log(`El área de un rectángulo con ancho ${width} y alto ${height} es: ${areaSquare(width, height)}.`)

// Área circulo
let radio = 10

const areaCircle = (radio) => Math.PI * Math.pow(radio, 2)

console.log(`El área de un círculo con radio ${radio} es: ${areaCircle(radio)}.`)