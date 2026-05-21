/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/* CICLO FOR  CLASICO - ITERACION DE LISTAS*/

//ITERAR ----> RECORRER UNA LISTA DE ELEMENTOS
//ITERAR ----> DE FORMA SECUENCIAL


/*
ESTRUCTURA EN JAVA SCRIPT

for (INICIALIZACION; CONDICION; INCREMENTO) {
    //CODIGO A EJECUTAR
}
*/  

const listaDeProfes = ["edward", "abdul", "eliana", "matu"]
// [] --> array vacio / lista

console.log ("TAMAÑO:", listaDeProfes.length) //TAMAÑO 4
console.log (listaDeProfes[2]) //IMPRIME A ELIANA
console.log ("-------------------------------------------")

for (i= 0; i < listaDeProfes.length; i++ /* i + 1 */){
    /* que i sea menor a la ultima posicion*/
    console.log (listaDeProfes[i])
}

/* CICLO FOR  FOR OF*/

// FOR IF ---> SE UTILIZA PARA COSAS ITERABLR(SE PUEDEN RECORRER)
// FOR OF ---> ARRAY Y STRING
console.log ("-------------------------------------------")
const listaDeFrutas = ["manzana", "pera", "piña", "mango"]

for (i of listaDeFrutas){
    console.log(i)
}

/* CICLO FOR  FOR IN*/

// FOR IN ---> SE UTILZA PARA COSAS ENUMERABLES
//FOR IN ---> OBJETC
console.log ("-------------------------------------------")

const tiendaDeCelulares = {
    iphone: 5,
    samsung: 8,
    huawei: 10,
    xiaomi: 200
}

for (i in tiendaDeCelulares){
    console.log(i) //IMPRIME LAS CLAVES
    console.log(tiendaDeCelulares[i]) //IMPRIME LOS VALORES
    console.log(`${i}: ${tiendaDeCelulares[i]}`) //IMPRIME CLAVE Y VALOR
}

