const carrito = [ 'Producto 1', 'Producto 2', 'Producto 3' ]
console.log(carrito)

const appContenedor = document.querySelector('#app')

let html = ''

carrito.map(producto =>  html += `<li>${producto}</li>`)

appContenedor.innerHTML = html