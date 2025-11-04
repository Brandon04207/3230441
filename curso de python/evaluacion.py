"""
nombre = str (input( "ingrese sus nombres:_ " ))
apellido = str (input( "ingrese sus apellidos:_" ))
id =  int (input( "ingrese su identificacion:_" ))
edad =  int (input( "ingrese su edad:_" ))
estatura = float (input( "ingrese su estatura:_ " ))
email = str (input( "ingrese su email:_ " ))

print ("su nombre es:_",nombre,"\n","su apelldio es:_",apellido,"su id es:_",id,"\n",
       "su edad es:_",edad,"\n","su estatura:_",estatura,"\n","su email:_",email)
"""

import random as r
numeroAleatorio = r.randint(0,10)
print(numeroAleatorio)

numero=int(input("adivina el numero:_"))

if numeroAleatorio == numero: 
    print("adivinaste")
elif numeroAleatorio != numero:
    # el != es para decir que no es igual
    print ("perdiste")
else:
    print ("no pusiste bien el numero, vuelve a intentarlo")
    


 

