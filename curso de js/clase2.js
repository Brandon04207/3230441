/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/*NUMEROS Y OPERACIONES MATEMATICAS*/

//1.tipo entero o decimal
const nuemroEntero = 25 //NUMBER 
const numeroDecimal = 3.5 //NUMBER

//2. notacion cientifica
const cientifica = 5e3 //5000 
console.log(cientifica)

//3.INFINITOS Y NAN 
const numeroInfinito = Infinity //NUMBER
console.log(typeof numeroInfinito)

const numeroNan = NaN
console.log (typeof numeroNan)

/*NUMEROS Y OPERACIONES MATEMATICAS*/

const suma = 5 + 9 //14
const resta = 10 - 8 //2
const division = 10 / 5 //2
const multiplicacion = 8 * 8 //64
const potencia = 2 ** 5 //32
const module = 5 % 2 //1

/*OPERACIONES AVANZANDAS MATH*/

const raizCuadrada = Math.sqrt(25)//5
const valorAbsoluto = Math.abs(-7)//7
const numeroAleatorio = Math.random () // [0 - 1]

console.log ("------------------------------------------")

console.log (raizCuadrada)
console.log (valorAbsoluto)
console.log (numeroAleatorio)
console.log ("------------------------------------------")
//precision 
const resultado= 0.1 + 0.2 // 0.3
console.log (resultado)
console.log (resultado.toFixed(1)) //se arregla, aqui cambia a String

console.log(resultado.toFixed == 0.3) //false
console.log(resultado.toFixed(1) == 0.3) //true
console.log(resultado.toFixed(1) === 0.3) // ("==="astracta) false



console.log ("------------------------------------------")

/*TYPE CASTIN O CONVERSION DE TIPO / COHERCION O PARSEO = cambiar tipo de dato */ 

//explicito
const numeroString = "42" //STRING
const numeroNumber = parseInt(numeroString) //NUMBER

console.log (numeroString, numeroNumber)
console.log (typeof numeroString, typeof numeroNumber)
console.log ("------------------------------------------")

const numeroFLoat = "3.4"
const floatNumber = parseFloat (numeroFLoat)
console.log (floatNumber)
console.log ("------------------------------------------")
const numeroBinario = "1111"
const binarioNumber = parseInt (numeroBinario, 2) 
console.log (binarioNumber)
console.log ("------------------------------------------")


//implicito

const sumaNumeros = "5" + 4 
console.log (sumaNumeros)
                            //SI HAY UN STRING, JAVASCRIPT CONCATENA

const sumabooleano = "8" + true 
console.log (sumabooleano)
                            //SI NO HAY UN STRING, JAVASCRIPT OPERA

console.log ("------------------------------------------")

const precision = 0.1 + 0.2
const precisionFIX = precision.tofixed (1) //type implicito

const precisionFIXNumber = parseFloat (precisionFIX)
console.log (typeof precisionFIXNumber, precisionFIXNumber)

const sumString = "25"
const sumNumero = 25
const sumbooleano = false 

console.log ("------------------------------------------")

console.log (sumString + sumString ) // concatena
console.log (sumString + sumNumero ) // concatena
console.log (sumString + sumbooleano ) // cancatena

console.log (sumNumero +sumNumero ) // concatena
console.log (sumNumero +sumNumero ) // opera
console.log (sumNumero + sumbooleano ) // opera

console.log (sumabooleano +sumString ) // concatena
console.log (sumabooleano +sumNumero ) // opera
console.log (sumabooleano +sumbooleano ) // opera