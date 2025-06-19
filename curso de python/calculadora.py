numero1 = float (input( "ingrese primer numero: " ))
numero2 = float (input( "ingrese segundo numero:" ))
operacion= (input("ingrese que operacion quiere hacer(suma(+), resta(-), multiplicacion(*), division(/), potencia(**):"))
#se crea otra variante para ingresar la operacion deseada

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
potencia = numero1 ** numero2

if operacion == "+" or operacion ==" suma":
    print (" la suma de:",numero1, "+",numero2," es:", suma)
    #si operacion es igual a suma/+ hacer esto
    
elif operacion == "-" or operacion =="resta":
    print ("la resta de:", numero1,"-",numero2,"es:", resta)
    # el "or" se utiliza para decir que si una de esas es verdadera hacer lo siguiente 

elif operacion == "*" or operacion =="multiplicacion":
    print ("la multiplicacion de:", numero1,"*",numero2,"es:", multiplicacion)
    # debemos hacer la comparacion completa cuando se una el or, si operacion es = a multiplicacion o operacion es = * hacer lo siguiente  
    
elif operacion == "/" or operacion =="division":
    if numero2 == 0:
        print ("no se puede dividor por cero" )
    else:
        division = numero1 / numero2
        print ("la division de:", numero1,"/",numero2,"es:", division)
        #pongo la division dentro del else para que primero vea la condicion y si no la cumple haga la division 

elif operacion == "**" or operacion =="potencia":
    print ("la potenciacion de:", numero1,"**",numero2,"es:", potencia)

else:
    print ( "poner correctamente los datos")