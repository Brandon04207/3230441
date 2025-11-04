minutosTotal= int(input("ingrese la cantidad de minutos:_"))

horas= minutosTotal //60
minutos= minutosTotal % 60
print (f"{minutosTotal} son: {horas} horas con {minutos} minutos")
#-------------------------------------------------------------------------------------------------------
numeroEntero= int(input("ingrese numero entero:_"))

print (f"la tabla de multplicar de{numeroEntero} es:" )
for i in range(1,11):
    resultado= i * numeroEntero
    input (f"{numeroEntero} * {i} = {resultado}")
    
#-------------------------------------------------------------------------------------------------------
valorCompra= float(input("digite el valor de la compra:_" ))

if valorCompra > 100000:
    descuento= valorCompra * 0.10
    
    print (f"el total a pagar es:_{descuento}") 
else:
    print (f"el total a pagar es:{valorCompra}")

#-------------------------------------------------------------------------------------------------------
numero1= int(input("digite pirmer numero entero:_"))
numero2= int(input("digite segundo numero entero:_"))
numero3= int(input("digite tercer numero entero:_"))

if numero1 > numero2 > numero3:
    print (numero1,"es mayor")
elif numero2 > numero3:
    print(numero2,"es mayor")
else:
    print(numero3,"es mayor")

#-------------------------------------------------------------------------------------------------------
n= int( input("digite numero:_"))

print ("los numeros de 1 al",n,"son:")
for i in range(1, n+1):
    if i %2 ==0:
        print(i,"es par")
    else:
        print(i,"es impar")
