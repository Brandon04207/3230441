/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

const nombres = ["Alejandro", "Sofía", "Miguel", "Valentina", "Sebastián"];

for (let i = 0; i < nombres.length; i++) {
  console.log(`Nombre: ${nombres[i]} | Caracteres: ${nombres[i].length}`);
}

console.log("--------------------------------------------------")

const frase = "Hola mundo";

for (const caracter of frase) {
  console.log(caracter);
}

console.log("--------------------------------------------------")

const frutas = ["manzana", "mango", "fresa", "uva", "sandía"];

for (const fruta of frutas) {
  console.log(`Me gusta la fruta: ${fruta}`);
}

console.log("--------------------------------------------------")

const producto = {
  nombre: "Auriculares Bluetooth",
  precio: 49.99,
  categoria: "Electrónica"
};

for (const propiedad in producto) {
  console.log(`${propiedad}: ${producto[propiedad]}`);
}

console.log("--------------------------------------------------")

const numeros = [10, 20, 30, 40, 50];

// Con for clásico
for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i]);
}

// Con for...of
for (const numero of numeros) {
  console.log(numero);
}