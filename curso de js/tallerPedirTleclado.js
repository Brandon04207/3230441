/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

const readline = require('readline') 
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
    })

const clavePredefinida = "1234"
intentos = 0

function verificarClave () {
    rl.question ("ingrese la clave: ", clave => {
        if (clave === clavePredefinida) {
            console.log ("clave correcta, accediendo al menu...")
            mostrarMenu()
        } else {
            intentos++
            if (intentos < 3) {
                console.log ("clave incorrecta, intente de nuevo")
                verificarClave()
            } else {
                console.log ("demasiados intentos fallidos, saliendo del programa...")
                rl.close()
            }
        }
    })

}

function mostrarMenu () {
    console.log ("-----------------------------")

    console.log ("menu principal")

    console.log ("------------------------------")

    console.log ("1. tabla de multiplicar")
    console.log ("2. verificar si un numero es par o impar")
    console.log ("3. salir")

    rl.question ("ingrese una opcion: ", opcion => {
        console.log ("------------------------------")

        if (opcion === "1") {
            rl.question ("ingrese un numero para mostrar su tabla de multiplicar: ", numero => {
                tablaDeMultiplicar(numero)
            })
        } else if (opcion === "2") {
            rl.question ("ingrese un numero para verificar si es par o impar: ", numero => {
                verificarParImpar(numero)
            })
        } else if (opcion === "3") {
            console.log ("saliendo del programa...")
            rl.close()
        } else {
            console.log ("opcion invalida, intente de nuevo")
            mostrarMenu()
        }
    })
}

function tablaDeMultiplicar (numero) {
    console.log ("tabla de multiplicar del", numero)
    for (let i = 1; i <= 10; i++) {
        console.log (numero, "x", i, "=", numero * i)
    }
    mostrarMenu()
}

function verificarParImpar (numero) {
    if (numero % 2 === 0) {
        console.log (numero, "es un numero par")
    } else {
        console.log (numero, "es un numero impar")
    }
    mostrarMenu()
}

verificarClave()


