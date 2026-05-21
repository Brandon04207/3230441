/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/* funciones */
/* reutilizar bloques de codigo */

/*
estructura
function nombraDeLaFuncion (PARAMETROS INICIALES){
    //codigo a ejecutar
}
  
nombreDeLaFuncion (PARAMETROS INICIALES)

*/

//SIN PARAMETROS INICIALES

function saludar(){
    console.log ("hola mundo")
}

saludar () //ejecutar la funcion

//CON PARAMETROS INICIALES

function saludo(nombre){
    console.log ("-------------------------------------")
    console.log("hola", nombre, "te quiero <3")  
}

saludo ("alejo") //ejecutar la funcion con el parametro

console.log("-------------------------------------------------------------------------------")
function suma (num1, num2){
    let resultado = num1 + num2
    console.log ("el resultado de la suma es:", resultado)
}

//funciones impuras e impuros

//ejemplo de funcion impura

function sumaDosNumeros(num1, num2){
    let resultado = num1 + num2
    return resultado
} 

console.log ("-------------------------------------------------------------------------------")
// tiene efectos secundarios, puede modificar algo fuera de la funcion, 
// no siempre devuelve el mismo resultado para los mismos parametros

//funcion pura
console.log ("-------------------------------------------------------------------------------")
function sumaDosNumerosPura(num1, num2){
    return num1 + num2
} 
// no tiene efectos secundarios, no modifica nada fuera de la funcion,
// siempre devuelve el mismo resultado para los mismos parametros
