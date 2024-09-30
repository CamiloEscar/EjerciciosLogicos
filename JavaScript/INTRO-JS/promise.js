
const aplicarDescuento = new Promise((resolve, reject) => {

    let descuento = true;

    if (descuento) {
        resolve('Descuento aplicado');
    } else {
        reject('No se pudo aplicar el descuento');
    }
});

console.log(aplicarDescuento);