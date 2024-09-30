const  lenguajes = [ 'JavaScript', 'PHP', 'Python' ];
const  frameworks = [ 'ReactJS', 'Laravel', 'Django', 'Ruby on Rails' ];

// unir los arreglos en un solo arreglo

// forma anterior
let combinacion = lenguajes.concat(frameworks);
console.log(combinacion);

// forma nueva
let combinacion2 = [...lenguajes, ...frameworks];
console.log(combinacion2);

// otros ejemplos
let [ultimo] = [...lenguajes].reverse()
console.log(ultimo);
