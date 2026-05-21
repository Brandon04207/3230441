/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/


const readline = require('readline') 
// readline es un modulo de node que nos permite leer lo que el usuario ingresa por teclado, para eso se necesita crear una interfaz de lectura (readline interface) y luego usarla para preguntar al usuario lo que queremos saber.

const rl = readline.createInterface({ // para abreviar readline (rl)
    input: process.stdin,
    output: process.stdout
    // process.stdin es la entrada estándar (lo que el usuario escribe) y process.stdout es la salida estándar (lo que se muestra en la consola)
})

//ESTRUCTURA

// para llamar usuario por teclado es:

rl.question ("ingrese su nombre?", nombreDeUsuario => {
    //CODIGO A EJECUTAR
    console.log(`hola! ${nombreDeUsuario} estas muy guap@ bb.`)
     rl.close()
})     



rl.question ('ingrese su edad: ', edadDeUsuario => {
    edadnNumero= parseInt(edadDeUsuario) // parseInt convierte el string ingresado por el usuario a un numero entero, si el usuario ingresa algo que no se puede convertir a numero, parseInt devuelve NaN (Not a Number)

    console.log (`tu edad es: ${edadnNumero +1}`)
    rl.close() // rl.close() cierra la interfaz de lectura
})



rl.question ('ingrese sunombre: ', nombreDeUsuario => {
    rl.question ('ingrese su edad: ', edadDeUsuario => {
        edadnNumero= parseInt(edadDeUsuario) 
        console.log (`hola! ${nombreDeUsuario} estas muy guap@ bb, tu edad es: ${edadnNumero }`)
        rl.close() 
    })
})
//anidado = en cadena // para preguntar varias cosas al usuario, se pueden anidar varias preguntas dentro de la función de callback de rl.question, esto se conoce como anidamiento (nesting) y permite hacer preguntas secuenciales al usuario.