/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/* OPERACIONES DE COMPARACION */

/* 
== --> compara si es abstractamente que --> valor 
=== --> compara si es escrictamente que --> valor y tipo de dato
!= --> compara si es astractamente diferente --> valor 
!== --> compara si es astractamente diferente --> valor tipo
< --> compara si es menor que
> --> compara si es mayor que
<= --> compara si es menor o igual que
>= --> compara si es mayor o igual que
*/

/* ejemplo */
const numeroUno = 10
const numeroDos = "10"
const numeroTres = 20
const numeroCuatro = "20"
const numeroCinco = 30
const numeroSeis = 40
const numeroSiete = 10

console.log(numeroUno == numeroDos) //true
console.log (numeroTres === numeroCuatro) //false
console.log ("------------------------------------------------")
console.log (numeroSeis != numeroUno) //true
console.log (numeroTres !== numeroCuatro) //true
console.log (numeroSiete !== numeroUno) //false
console.log (100 !== 100) // false 
console.log ("50" !== 50) // true
console.log ("3.14" != 3.14) // false 
console.log ("------------------------------------------------")
console.log (numeroSeis > numeroCinco) // true
console.log (numeroTres < numeroSeis) // true
console.log (numeroSeis < numeroDos) // false = cumple valor 
console.log (numeroCuatro >= numeroTres) // true
console.log (numeroSeis <= numeroDos) // false
console.log (-7 < 10) // true

/* OPERACIONES LOGICOS */

/*
 && ---> and o y ---> para obtener true, todas las condiciones deben ser: true  
 || ---> or o u ---> para obtener un true, solo una condicion deben ser: true
 ! ---> not o no ---> niega la salida ---> true! = false
*/

/* ejemplo */
const numeroA= 10
const numeroB= "10"
const numeroC= 20
const numeroD= "20"
const numeroE= 30
const numeroF= 40

//operador logico and (&&) ---> true, todas deben ser verdaderas
console.log ("------------------------------------------------")
console.log  (numeroA == numeroB && numeroE < numeroF)//true 
console.log  (numeroA < numeroB && numeroA == numeroB && numeroE < numeroF)//false 
console.log ("------------------------------------------------")

//operador logico or (||) ---> true, almenos una debe ser verdadera
console.log  (numeroF !== numeroD || numeroF < numeroA || numeroC === numeroD ) //true 
console.log  (numeroE == numeroF || numeroF < numeroA || numeroC === numeroD || numeroA === numeroB ) //false 
console.log ("------------------------------------------------")

//operador logico not (!) ---> negacion 
console.log (!(numeroA == numeroB)) //false
console.log (!(!(numeroA > numeroB) && numeroA == numeroB && !(numeroE < numeroF))) //true 


