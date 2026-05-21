function sumar(){
    let num1 = document.getElementById("num1").value;//document es el objeto que representa el documento HTML
    let num2 = document.getElementById("num2").value;//getElementById es un método que permite acceder a un elemento del HTML a través de su id
    let resultado = document.getElementById("resultado")
    num1 = parseInt(num1);
    num2 = parseInt(num2);
    let resultadoSuma = num1 + num2;

    resultado.value = resultadoSuma; //value es una propiedad que permite obtener o establecer el valor de un elemento del HTML

    //lo que hace es asignar el resultado de la suma al valor del elemento con id "resultado", que es un campo de texto en el HTML,
    //  para mostrar el resultado al usuario.
}

function restar(){
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    let resultado = document.getElementById("resultado")

    num1 = parseInt(num1);
    num2 = parseInt(num2);
    let resultadoResta = num1 - num2;

    resultado.value = resultadoResta;
}

function multiplicar(){
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    let resultado = document.getElementById("resultado")
    
    num1 = parseInt(num1);
    num2 = parseInt(num2);
    let resultadoMultiplicacion = num1 * num2;

    resultado.value = resultadoMultiplicacion;
}

function dividir(){
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    let resultado = document.getElementById("resultado")

    num1 = parseInt(num1);
    num2 = parseInt(num2);
    
    if (num2 === 0) {
        alert("No se puede dividir por cero");
        resultado.value = "Error: División por cero";
        return;
    }

    let resultadoDivision = num1 / num2;

    resultado.value = resultadoDivision;
}

function calcular(){
    let nombre = document.getElementById("nombre").value;
    let cantidad = parseInt(document.getElementById("cantidad").value);
    let valorHoras = parseInt(document.getElementById("valorHoras").value);

    let resultado = cantidad * valorHoras;
    if (cantidad > 280) {
       let pago = resultado * 1.10;
       document.getElementById("resultado").innerHTML = "el empleado " + nombre + " se le debe pagar $" + pago.toFixed(0);
    } else {
        document.getElementById("resultado").innerHTML = "el empleado " + nombre + " se le debe pagar $" +resultado;
    }
}

function calcularprom(){

    let nombre = document.getElementById("nombre").value;
    let nota1 = parseInt(document.getElementById("nota1").value);
    let nota2 = parseInt(document.getElementById("nota2").value);
    let nota3 = parseInt(document.getElementById("nota3").value);
    let nota4 = parseInt(document.getElementById("nota4").value);

    let promedio = (nota1 + nota2 + nota3 + nota4) / 4;

    if (promedio <= 3.0) {
        document.getElementById("promedio").innerHTML = nombre+ "su promedio es:" + promedio+ "es basico.";
    }
    else if (promedio > 3.0 && promedio <= 4.0) {
        document.getElementById("promedio").innerHTML = nombre+ "su promedio es:" + promedio+ "es alto.";
    }
    else {
        document.getElementById("promedio").innerHTML = nombre+ "su promedio es:" + promedio+ "es superior.";
    }
}