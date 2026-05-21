
n = int(input("Ingrese un numero entero positivo: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
        
#--------------------------------------------

numeroEntero= int(input("ingrese numero entero:_"))

if numeroEntero <= 10:
    print (f"la tabla de multplicar de{numeroEntero} es:" )
    for i in range(1,11):
        print (f"{i} x {numeroEntero} = {i*numeroEntero}")
else:
    print (f"el numero{numeroEntero} no esta en el rango")

#--------------------------------------------


contadorPositivos= 0
contadorNegativos= 0
while True:
    numero= int(input("ingrese un numero (0 para salir): "))
    if numero == 0:
        break
    elif numero > 0:
        contadorPositivos += 1
    else:
        contadorNegativos += 1
print(f"Los números positivos ingresados son: {contadorPositivos}")
print(f"Los números negativos ingresados son: {contadorNegativos}")

#-------------------------------------------------------------
intetentos= 0
contador= 0
while contador < 3:
    contraseña= input("ingrese la contraseña: ")
    if contraseña == "contraseña123":
        print("contraseña correcta")
        break 
    else:
        print("contraseña incorrecta")
        intetentos += 1
        contador += 1