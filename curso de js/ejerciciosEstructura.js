/*-----------------------------------------*/
/* Brandon Alejandro Diaz Arango - 18 años de edad */
/* estudiante sena - analisis y desarrollo de sofware*/
/* de Bello antioquia, brandon04207@gmail.com*/
/*------------------------------------------*/

/*condicionales if y switch */
const edad = 25; // Puedes cambiar este valor para probar

if (edad < 12) {
    console.log("Eres un niño.");
} else if (edad >= 12 && edad <= 17) {
    console.log("Eres un adolescente.");
} else if (edad >= 18 && edad <= 59) {
    console.log("Eres un adulto.");
} else {
    console.log("Eres un adulto mayor.");
}
console.log("------------------------------------------------")

const numero1 = 10;
const numero2 = 5;

if (numero1 > numero2) {
    console.log("El primer número es mayor");
} else if (numero2 > numero1) {
    console.log("El segundo número es mayor");
} else {
    console.log("Ambos números son iguales");
}
console.log("------------------------------------------------")

const rol = 'editor'; 

if (rol === 'admin') {
    console.log("Bienvenido, administrador.");
} else if (rol === 'editor') {
    console.log("Acceso como editor concedido.");
} else if (rol === 'invitado') {
    console.log("Acceso limitado.");
} else {
    console.log("Rol no reconocido. Acceso denegado.");
}
console.log("------------------------------------------------")

const opcion = 2; // Valor entre 1 y 4

switch (opcion) {
    case 1:
        console.log("Ver perfil");
        break;
    case 2:
        console.log("Editar perfil");
        break;
    case 3:
        console.log("Ver notificaciones");
        break;
    case 4:
        console.log("Salir");
        break;
    default:
        console.log("Opción no válida");
}
console.log("------------------------------------------------")

const dia = "lunes".toLowerCase(); // Día en minúsculas

switch (dia) {
    case "lunes":
    case "martes":
    case "miércoles":
    case "miercoles": // Sin acento también
    case "jueves":
    case "viernes":
        console.log("Es un día laboral.");
        break;
    case "sábado":
    case "sabado": // Sin acento también
    case "domingo":
        console.log("Es un día de descanso.");
        break;
    default:
        console.log("Día no reconocido.");
}
console.log("------------------------------------------------")

const color = "azul".toLowerCase(); // Puede ser cualquier color

switch (color) {
    case "rojo":
    case "azul":
    case "amarillo":
        console.log("Es un color primario.");
        break;
    default:
        console.log("No es un color primario.");
}



