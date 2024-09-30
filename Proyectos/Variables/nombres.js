// https://github.com/andersontr15/clean-code-javascript-es
// Variables
// Utiliza nombres significativos y pronunciables para las variables

// Mal hecho:
const yyyymmdstr = moment().format('YYYY/MM/DD');

// Bien hecho:
const fechaActual = moment().format('YYYY/MM/DD');

// Utiliza el vocabulario igual para las variables del mismo tipo
// Mal hecho:
conseguirInfoUsuario();
conseguirDataDelCliente();
conseguirRecordDelCliente();

// Bien hecho:
conseguirUsuario();

// Utiliza nombres buscables
// Nosotros leemos mucho más código que jamás escribiremos. Es importante que el código que escribimos sea legible y buscable. Cuando faltamos nombrar a las variables de manera buscable y legible, acabamos confundiendo a nuestros lectores. Echa un vistazo a las herramientas para ayudarte: buddy.js y ESLint

// Mal hecho:
// Para qué rayos sirve 86400000? 
setTimeout(hastaLaInfinidadYMasAlla, 86400000);

// Bien hecho:
// Decláralos como variables globales de 'const'.
const MILISEGUNDOS_EN_UN_DIA = 8640000;

setTimeout(hastaLaInfinidadYMasAlla, MILISEGUNDOS_EN_UN_DIA);

