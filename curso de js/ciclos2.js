/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/* ciclo while - loop*/

/* 
ESCRUCTURA 

WHILE (CONDICION){
    //CODIGO A EJECUTAR
    //CONTADOR 

}
*/

//EJEMPLO

let contador = 0

while (contador < 10){
    console.log ("valor:",contador)
    contador++

}

console.log("-------------------------------------------------------------------------------")

//decremento
let numero = 5
console.log (numero--) //es un 5 y decrementa
console.log (numero) //ya es un 4

console.log("-------------------------------------------------------------------------------")

//LIMITE DE SEGURIDAD 
 
let limiteDeSeguridad = 3
while(limiteDeSeguridad --> 0){
    console.log ("valor atual:", limiteDeSeguridad)
    //no hay contador!!!!!!
}

console.log("-------------------------------------------------------------------------------")

let liminteDeSeguridadDOS = 1000
let contadorDos = 0

while (contadorDos < 10 && liminteDeSeguridadDOS -- > 0){
    console.log ("valor actual:", contadorDos)
    contador ++ 
} 
console.log("-------------------------------------------------------------------------------")

/* ciclo do while - loop*/
//do = hacer
/*
estrucura 

DO{
    //CODIGO A EJECUTAR
    //CONTADOR ++

}WHILE(CONDICION)


*/

//ejecuta primero y luego evalia 

//ejemplo 
let contadorTres = 0

do{
    console.log (contadorTres)
    contadorTres ++

}while (contadorTres > 10 )

/*
1. suponer una variante edadDeUsuario = 20
2. imprimir un mensaje solo si la persona es menor de edad
    (edadDEUsuario < 18)
3. while y do while 
*/

console.log("-------------------------------------------------------------------------------")

let edadDeUsuario = 20
while (edadDeUsuario <18){
    console.log ("eres menor de edad, tienes:",edadDeUsuario,",con while")
    edadDeUsuario ++
}

do{
    console.log ("eres menor de edad, tienes:",edadDeUsuario, ",con do while")
    edadDeUsuario ++
} while (edadDeUsuario < 18)


