"""
saldo = 1000  

while True:
    print("Bienvenido al cajero automático.")
    print("Por favor, seleccione una opción:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Consignar dinero")
    print("4. Salir")
    
    opcion = int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        print(f"Su saldo actual es: ${saldo}")
    
    elif opcion == 2:
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        if monto_retiro > saldo:
            print("Lo siento, su saldo es insuficiente para realizar este retiro.")
        else:
            saldo -= monto_retiro
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
    
    elif opcion == 3:
        monto_consignacion = float(input("Ingrese el monto a consignar: "))
        saldo += monto_consignacion
        print(f"Consignación exitosa. Su nuevo saldo es: ${saldo}")
    
    elif opcion == 4:
        print("Gracias por usar nuestro cajero automático. ¡Hasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        
"""

"""
numero = int(input("Ingrese un número entero: "))

# Convertir el número a una cadena, luego invertir la cadena y convertirla de vuelta a un número
numero_invertido = int(str(numero)[::-1])

print(f"El número {numero} al revés es: {numero_invertido}")

"""