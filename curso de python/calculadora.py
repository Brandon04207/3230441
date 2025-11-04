while True:
    numero1 = float (input( "ingrese primer numero:_ " ))
    numero2 = float (input( "ingrese segundo numero:_" ))
#variante uno y dos para poner los numeros, float para poner numero decimales
    operacion= (input("ingrese que operacion quiere hacer(suma(+), resta(-), multiplicacion(*), division(/), potencia(**):_"))
#se crea otra variante para ingresar la operacion deseada

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    potencia = numero1 ** numero2
#hago que las dos variantes hagan todas las operaciones menos la division porque primero debe leer la condicion 


    if operacion == "+" or operacion ==" suma":
        print (" la suma de:_",numero1, "+",numero2," es:_", suma)
    #si operacion es igual a suma/+ hacer esto
    
    elif operacion == "-" or operacion =="resta":
        print ("la resta de:_", numero1,"-",numero2,"es:_", resta)
    # el "or" se utiliza para decir que si una de esas es verdadera hacer lo siguiente 

    elif operacion == "*" or operacion =="multiplicacion":
        print ("la multiplicacion de:_", numero1,"*",numero2,"es:_", multiplicacion)
    # debemos hacer la comparacion completa cuando se una el or, si operacion es = a multiplicacion o operacion es = * hacer lo siguiente  
    
    elif operacion == "/" or operacion =="division":
        if numero2 == 0:
            print ("no se puede dividor por cero" )
        else:
            division = numero1 / numero2
            print ("la division de:_", numero1,"/",numero2,"es:_", division)
        #pongo la division dentro del else para que primero vea la condicion y si no la cumple haga la division 

    elif operacion == "**" or operacion =="potencia":
        print ("la potenciacion de:", numero1,"**",numero2,"es:_", potencia)

    else:
        print ( "no has puesto los datos correctamente, vuelve aintentarlo")
        
        
    salir = (input("quiere salir de la calculadora (si , no)"))
    if salir == "si":
        break
    else:
        print ("gracias por utilizar la calculadora")
    
    
    