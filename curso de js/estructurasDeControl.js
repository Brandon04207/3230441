/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/*condicionales if y switch */

/* if - else if - else */

/* ESTRUCTURA

IF (CONDICION) {
    //CODIGO A EJECUTAR
    
}
ELSE{
    //CODIGO A EJECUTAR
}
-------------------------------
IF(CONDICION){
    //CODIGO A EJECUTAR
}
ELSE IF(CONDICION){
    //CODIGO A EJECUTAR
}
ELSE IF(CONDICION){
    //CODIGO A EJECUTAR
}
ELSE 
    //CODIGO A EJECUTAR

*/

//EJEMPLO

const edadPersona = 21
const generoDePersona = "femenino"

if (edadPersona >=18 && generoDePersona === "masculino"){
    console.log("usted ya puede ir a la carcel de hombres")
}
else if (edadPersona <18 && generoDePersona === "masculino"){
    console.log("usted puede ir a la correcional de hombres")
}
else if (edadPersona >=18 && generoDePersona === "femenino"){
    console.log("usted puede ir a la correcional de mujeres")
}
else if (edadPersona <18 && generoDePersona === "femenino"){
    console.log("usted puede ir a la correcional de mujeres")
}
else{
console.log("no se para donde vas")
}

 console.log ("-------------------------------------------------------")
// EJEMPLON 2

const idPersona = "NESTOR".toLowerCase()
if (idPersona === "alejo"){
    console.log ("hola!! bienvenido => alejo")
}
else if(idPersona === "nestor"){
    console.log ("hola!! bienvenido => nestor")
}
else{
    console.log ("acceso denegado")
}


/* swith case */

/*
ESTRUCTURA

SWICTH (VARIABLE){

    CASE VALOR1:
        //CODIGO A EJEJCUTAR
        //BREAK

    CASE VALOR2:
        //CODIGO A EJEJCUTAR
        //BREAK

    CASE VALOR3:
        //CODIGO A EJEJCUTAR
        //BREAK

    DEFAULT: 
        //CADIGO A EJECUTAR
        //BREAK
}

*/

//ejemplo
console.log ("---------------------------------------------------")

const canastaDeFrutas = "fresa".toLowerCase()

switch (canastaDeFrutas){
    case "tomate": 
        console.log ("el tomate cuesta $100")
        break
    case "mango": 
        console.log ("el mango cuesta $200")
        break
    case "pera": 
        console.log ("la pera cuesta $300")
        break
    case "fresa": 
        console.log ("la fresa cuesta $400")
        break
    case "aguacate": 
        console.log ("el aguacate cuesta $500")
        break
    default:
        console.log (`no hay disponible ${canastaDeFrutas} en estos momentos`)
        break
}
    