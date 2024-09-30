// Funcion Declaration

function saludar(nombre) {
    console.log(`Bienvenido: ${nombre}`);
}

saludar('Juan');

//function expression

const cliente = function(nombreDev, skill) {
    console.log(`Mostrando datos del Desarrollador: ${nombreDev}, ${skill}`);
}

cliente('Ernesto Ledesma', 'Desarrollador Web');