
    
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

#----------------------------------------------------------------------

num = int(input("Ingresa un número: "))

print(f"Los divisores de {num} son:")
for i in range(1, num+1):
    if num % i == 0:
        print(i)
#-----------------------------------------------------------------

num = int(input("Ingresa un número: "))

divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i

if divisors_sum == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")
    
#-----------------------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Ingresa un número entero positivo: "))
resultado = factorial(num)
print(f"El factorial de {num} es {resultado}")

#-------------------------------------------------------------------

def es_palindromo(num):
    # Convertir el número a una cadena de texto
    num_str = str(num)
    
    # Comparar la cadena con su reversa
    if num_str == num_str[::-1]:
        return True
    else:
        return False

numero = int(input("Ingresa un número: "))
if es_palindromo(numero):
    print(f"El número {numero} es palíndromo.")
else:
    print(f"El número {numero} no es palíndromo.")