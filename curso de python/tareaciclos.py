#1
"""   
acumulador = 0
contador =1
numeros= 0
while contador <= 30:
    numeros += 1
    if numeros %2 !=0 :
        acumulador += 1
    contador +=1
print ("los numeros impares son:_",acumulador)
"""

#2
"""
suma = 0
i = 1

while i <=10:
    numero=int(input("digite un numero entero:_"))
    suma += numero
    i = i+1
    
print ("la suma de los numeros es:_ ", suma)
"""

#3
"""
acomulador = 0
contador= 1
while contador <= 10:
    nombre = input("ingrese su nombre:"). upper ()
    
    if nombre == "JUAN":
        acomulador += 1
    contador += 1
    
if acomulador ==1:
    print ("el nombre Juan due dijitado",acomulador,"vez")
    
else:
    print ("el nombre Juan due dijitado",acomulador,"veces")
    
"""

#4
"""
import random as r

acumulador = 0
contador = 1
sumaDinero = 0

while contador <= 5:
    dinero = int (input("ingrese una cantidad de dinero:_"))
    

    n1= r.randint(0,4)
    n2= r.randint(0,4)
    n3= r.randint(0,4)

    print ("los numeros son:_",n1,n2,n3)

    if n1==n2 and n1==n3:
        sumaDinero = sumaDinero + dinero * 3
        print ( "usted gano el triple, dinero en total:_", sumaDinero )
        
    
    elif n1 == n2 or n1 == n3 or n2 == n3:
        sumaDinero = sumaDinero + dinero * 1.50
        print ( "usted gano la mitad, dinero en total:_",sumaDinero)

    else:
        sumaDinero = sumaDinero + dinero
        print ( "no gano nada, dinero en total:_",sumaDinero)
        
    contador += 1 
"""

#5
"""
acumulador = 0
contador = 1

trabajadores = int(input("cuantos trabajadores hay:_"))

while contador <= trabajadores:
    nombre = input ("ingrese su nombre:_")
    edad =int (input ("ingrese su edad:_"))
    salario =int (input ("ingrese su salario:_"))
    gastosMensuales =int (input ("ingrese sus gastos mensuales:_"))
    
    totalGastos = salario - gastosMensuales

    print (nombre," tu salario resustante es de:_", totalGastos, "pesos")
    
    if totalGastos < 0:
         acumulador += 1
    
    contador +=1
if acumulador == 1:
    print ("un trabajador gasta mas a su salario")
else:
    print (acumulador,"trabajadores gastan mas a su salario") 
"""