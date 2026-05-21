/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/


function saludarUsuario (nombre) {
    console.log ("hola", nombre, "bienvenido/a")
}

saludarUsuario ("Brandon")

console.log("-------------------------------------------------------------------------------")

function sumar (num1, num2){
    let resultado = num1 + num2
    console.log ("el resultado de la suma es:", resultado)
}

sumar (5, 10)

console.log("-------------------------------------------------------------------------------")

function calcularAreaTriangulo (base, altura){
    let area = (base * altura) / 2
    console.log ("el area del triangulo es:", area)
}

calcularAreaTriangulo (10, 5)

console.log("-------------------------------------------------------------------------------")

function convertirCelsiusAFahrenheit (celsius){
    let fahrenheit = (celsius * 9/5) + 32
    console.log (celsius, "grados Celsius son", fahrenheit, "grados Fahrenheit")
}

convertirCelsiusAFahrenheit (25)
 
console.log("-------------------------------------------------------------------------------")

function esPar (numero) {
    if (numero % 2 === 0) {
        console.log (numero, "es par")
    } 
    else {
        console.log (numero, "es impar")
    }
}

esPar (10)
esPar (7)

console.log("-------------------------------------------------------------------------------")

function calcularPrecioConIva (precio, iva) {
    let precioConIva = precio + (precio * iva / 100)
    console.log ("el precio con IVA es:", precioConIva)
}

calcularPrecioConIva (100, 19)

console.log("-------------------------------------------------------------------------------")

function tablaDeMultiplicar (numero) {
    console.log ("tabla de multiplicar del", numero)
    for (let i = 1; i <= 10; i++) {
        console.log (numero, "x", i, "=", numero * i)
    }
}

tablaDeMultiplicar (5)

