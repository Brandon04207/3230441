/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/

//imprimir en pantalla/consola
console.log ("pecho y espalda")

//node para imprimir en pantalla y clear para borrar 

/*---------------------------------------------------------------*/
/*variable: caja donde voy a guardar cosas, depende de la caja */
/*--------------------------------------------------------------*/

//VARIABLES Y BUENAS PRACTICAS

let cofreDeAndy = "woody"
// declaracion = asignacion 

//no esta permitido 
let c = "woody"
let cda = "woody"
let cAndy = "wody"

//si esta permitido
let primerJugueteDeAndy = "woody"
let urlInstagramAlejo = "https://www.instagram.com/4lejo_07/"
let cedulaDeAprendicesAdso = "1034286785"

//LET - variables que pueden cambiar en el tiempo
let contador = 0 

//CONST - variables que no pueden cambiar en el tiempo
const numeroPi = 3.1416

//TIPOS DE DATOS - PRIMITIMOS Y COMPLEJOS

/*
PIMITIVOS 
String 
Number 
Boolean
Null
Undefined
Symbol
Bigint

COMPLEJOS 
Array - lista ordenada de elementos, de forma secuencial
Object - tienen propiedad o valores, tambien como claves 
Function - se utiliza para reciclar bloques de codigo
*/


//EJEMPLOS PRIMITIVOS
let nombereDeUsuario = "Alejo" //string 
let edadDeUsuario = 27 //Number
let esMayorDeEdad = true //boolean
let valorNulo = null // null - ausencia de valor 
let valorIndefinido = undefined //undefined 
let simboloUnico = Symbol ("unico")//Symbol
let numeroGrande = 2n //bigint

console.log ("-----------------------------------------------------------")
console.log(typeof nombereDeUsuario, nombereDeUsuario) //typeof para ver que tipo de dato es 
console.log(typeof edadDeUsuario, edadDeUsuario)
console.log(typeof esMayorDeEdad, esMayorDeEdad)
console.log(typeof valorNulo, valorNulo)
console.log(typeof valorIndefinido, valorIndefinido)
console.log(typeof simboloUnico, simboloUnico)
console.log(typeof numeroGrande, numeroGrande)

//EJEMPLOS COMPLEJOS 
let listaDeFruta = ["mango", "piña", "manzana verde", "pera", "fresa", "uva"] //array
let profesorNestor = {
    nombre: "nestor",
    edad: 27,
    ciudad: "pereira",
    sexo: "M"

} //object
let funcion= function nombreDeLaFuncion(){}//function
console.log ("-----------------------------------------------------------")
console.log(typeof listaDeFruta,listaDeFruta)
console.log(typeof profesorNestor,profesorNestor)
console.log(typeof funcion, funcion)
console.log (Array.isArray(listaDeFruta))


//MANIPULACION DE STRINGS

let stringUNO = 'hola'
let stringDOS = "bb"
let stringTRES = `quiero verte`
let stringCUATRO =  `${stringUNO} ${stringDOS} ${stringTRES}`

console.log ("-----------------------------------------------------------")
console.log (stringUNO)
console.log (stringDOS)
console.log (stringTRES)
console.log (stringCUATRO)

//CONCATENAR 
console.log ("-----------------------------------------------------------")
console.log (stringUNO + stringDOS)
console.log (stringUNO, stringDOS)

let frase = "el viernes full perreo obceno,only +18,   ¡dulcinea!"

console.log (frase.length)//TAMAÑO
console.log (frase.toLowerCase()) //minuscula
console.log (frase.toUpperCase())//mayuscula
consele.log (frase.substring(42, 52))