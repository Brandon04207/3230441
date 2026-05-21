import random as r

# Generar lista aleatoria fuera de las funciones
lista = []
for i in range(3):
    numero = r.randint(0, 50)
    lista.append(numero)

# Ejercicio 1
def sumaNumeros():
    suma = 0
    for numero in lista:
        suma += numero
    print(lista)
    print("La suma de los números es:", suma)
    print("----------------------------------------------------------------")
    return suma

# Ejercicio 2
def sumaPares():
    sumaPares = 0
    for numero in lista:
        if numero % 2 == 0:
            sumaPares += numero
    print("La suma de los números pares es:", sumaPares)
    print("----------------------------------------------------------------")
    return sumaPares

# Ejercicio 3
def sumarPrimerElemento():
    print(f"Sumando el primer elemento ({lista[0]}) a cada número:")
    for numero in lista:
        print(f"{numero} + {lista[0]} = {numero + lista[0]}")
    print("----------------------------------------------------------------")

# Ejercicio 4
def buscarNumero():
    ingresarNumero = int(input("Ingrese un número: "))
    if ingresarNumero in lista:
        print("True")
    else:
        print("False")
    print("----------------------------------------------------------------")
    return ingresarNumero in lista

# Ejercicio 5
def verificarDuplicados():
    tiene_duplicados = len(lista) != len(set(lista))
    if tiene_duplicados:
        print("True (Hay duplicados)")
    else:
        print("False (No hay duplicados)")
    print("----------------------------------------------------------------")
    return tiene_duplicados

# Ejercicio 6
def frutasConA():
    listaFrutas = ["aguacate", "cereza", "ciruela", "arándano", "durazno", 
                   "fresa", "kiwi", "mango", "albaricoque", "manzana"]
    frutasPorA = []
    for fruta in listaFrutas:
        if fruta.startswith("a"):
            frutasPorA.append(fruta)
    print("Frutas que comienzan con 'a':", frutasPorA)
    return frutasPorA


print("Lista aleatoria generada:", lista)
print("=" * 64)
    
# Ejercicio 1
print("EJERCICIO 1: Suma de números")
sumaNumeros()
    
# Ejercicio 2
print("EJERCICIO 2: Suma de números pares")
sumaPares()
    
# Ejercicio 3
print("EJERCICIO 3: Sumar primer elemento")
sumarPrimerElemento()
    
# Ejercicio 4
print("EJERCICIO 4: Buscar número en lista")
buscarNumero()
    
# Ejercicio 5
print("EJERCICIO 5: Verificar duplicados")
verificarDuplicados()
    
# Ejercicio 6
print("EJERCICIO 6: Frutas que comienzan con 'a'")
frutasConA()

