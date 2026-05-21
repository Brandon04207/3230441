/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

const { CONNREFUSED } = require("node:dns")


/* array: propiedad , acceso y programacion */

/* array: es una estructura de datos que permite almacenar una coleccion de elementos, 
cada elemento se identifica por un indice numerico, el primer elemento tiene indice 0,
el segundo elemento tiene indice 1, y asi sucesivamente. */


//1. SINTAXIS LITERAL [] --> tipo de dato complejo / estructura de datos
const numeroUnico = [2]
console.log(numeroUnico, typeof numeroUnico) // [2] object

const arrayVacio = []
console.log (arrayVacio, typeof arrayVacio) // [] object

//TAMAÑO
//POSICION

//2. CONSTRUCTOR ARRAY()
const listaDeProfes = Array ("maturana", "edward", "abdul", "juliana", "yenny") // el tamaño es 5, la posicion va de 0 a 4
console.log (Array.isArray(listaDeProfes)) // true
console.log (listaDeProfes) // [ 'maturana', 'edward', 'abdul', 'juliana', 'yenny' ] object
/* (Array.isArray()) es un metodo estatico que se utiliza para verificar si un valor es un array,
devuelve true si el valor es un array y false si no lo es. */

const numetosEnteros = Array (1, 2, 3, 4, 5)
console.log (numetosEnteros) // [ 1, 2, 3, 4, 5 ] object

const unSoloNUmero = Array (7)
console.log (unSoloNUmero) // [ <7 empty items> ] object
/* cuando se utiliza el constructor Array con un solo numero, 
se crea un array con ese numero de elementos vacios, en este caso se crea un array con 7 elementos vacios. */

console.log ("-------------------------------------------")

//3. array mixto
const arrayMixto = [1, "texto", false, {
    nombre : "alejo",
    edad : 19,
    sexo : "masculino"
}, 2828, "holaa", ["aaa", true, 123]
]
console.log (arrayMixto.length) // 7
//para saber el tamaño de un array, se utiliza la propiedad length, esta propiedad devuelve el numero de elementos que tiene el array.

console.log (arrayMixto[6].length)
console.log (arrayMixto[6][1])// true
console.log ("-------------------------------------------")

//--------------------------------------------------------------
/* ARRAY: MUTABILIDAD */

const listaDeAprendices = ["viviana", "nikol", "alejo", "juli", "oween","daiver"]

listaDeAprendices.push ("jhonatan")// push añade un nuevo elemento al array, metodo mutable
console.log (listaDeAprendices)
console.log ("-------------------------------------------")

/* ARRAY: INMUTABILIDAD */

const nuevoAprendiz = listaDeAprendices.concat ("linda", "laura")
console.log ("ORIGINAL:", listaDeAprendices) 
console.log ("NUEVO:", nuevoAprendiz)
console.log ("-------------------------------------------")


//ejercicio practico: suma de todos los numeros [1 - 5], usando array ()

console.log ("-------------------------------------------")
console.log ("ejercicio ")

const numeros = Array (1, 2, 3, 4, 5)
let suma = 0

for (i = 0; i < numeros.length; i++){ 
    suma = suma + numeros[i]

}
console.log ("la suma de los numeros es:", suma)

console.log ("-------------------------------------------")

/* METODO PUSH Y POP */

//PUSH 
const listaDePaises = ["España", "Peru","Mexico","Italia"]
const nuevoPais = listaDePaises.push ("Venezuela")

console.log ("ORIGINAL: ", listaDePaises) // es mutable 
console.log ("TAMAÑO: ", nuevoPais) //muestra el tamaño

console.log ("-------------------------------------------")

//pop 
const eliminarPais = listaDePaises.pop() //elimina el ultimo elemento
console.log ("ORIGINAL", listaDePaises)
console.log (eliminarPais)//devuelve en pantalla lo que elimino

const arrayEmpty = []
const eliminaArrayEmpty = arrayEmpty.pop()
console.log (eliminaArrayEmpty)




