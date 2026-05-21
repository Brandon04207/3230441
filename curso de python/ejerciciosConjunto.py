numeros = set()
while True:
    entrada = input("Ingrese un número o 'fin' para terminar: ")
    if entrada.lower() == "fin":
        break
    else:
        numeros.add(int(entrada))
        
print("Números únicos ingresados:", numeros)
print("Cantidad total de elementos únicos:", len(numeros))
#len devuelve la cantidad de elementos únicos en el conjunto numeros.

print ("--------------------------------------------------------")

aprendices = set()
while True:
    nombre = input("Ingrese el nombre del aprendiz o 'fin' para terminar: ")
    if nombre.lower() == "fin":
        break
    else:
        aprendices.add(nombre)
        print(aprendices)
print("Aprendices correctamente matriculados:", aprendices)

print ("--------------------------------------------------------")

programacion = set()
basesDeDatos = set()

cantidadprogramacion = int(input("Ingrese la cantidad de aprendices inscritos en Programación: "))

for i in range(cantidadprogramacion):
    nombre = input("Ingrese el nombre del aprendiz inscrito en Programación: ")
    programacion.add(nombre)
    
cantidadbasesDeDatos = int(input("Ingrese la cantidad de aprendices inscritos en Bases de Datos: "))

for i in range(cantidadbasesDeDatos):
    nombre = input("Ingrese el nombre del aprendiz inscrito en Bases de Datos: ")
    basesDeDatos.add(nombre)
    
print("Aprendices inscritos en ambos cursos:", programacion & basesDeDatos)
print("Aprendices solo en Programación:", programacion - basesDeDatos)
print("Aprendices solo en Bases de Datos:", basesDeDatos - programacion)

print ("--------------------------------------------------------")

usuarios_autorizados = {"juan", "maria", "pedro", "ana"}
nombre_usuario = input("Ingrese su nombre de usuario: ").lower()
if nombre_usuario in usuarios_autorizados:
    #in es para verificar si el nombre_usuario pertenece al conjunto usuarios_autorizados, devuelve True o False.
    print("Acceso permitido")
else:
    print("Acceso denegado")
    
print ("--------------------------------------------------------")
pares = set()
impares = set()

while True:
    entrada = input("Ingrese un número o 'fin' para terminar: ")
    if entrada.lower() == "fin":
        break
    else:
        numero = int(entrada)
        if numero % 2 == 0:
            pares.add(numero)
        else:
            impares.add(numero)

print("Números pares:", pares)
print("Números impares:", impares)

print("---------------------------------------------------------")

productos_vendidos = set()
while True:
    producto = input("Ingrese el nombre del producto vendido o 'fin' para terminar: ")
    if producto.lower() == "fin":
        break
    else:
        productos_vendidos.add(producto)
print("Productos vendidos:", productos_vendidos)
eliminar_producto = input("Ingrese el nombre del producto a eliminar del inventario: ")
if eliminar_producto in productos_vendidos:
    productos_vendidos.remove(eliminar_producto)
    print("Producto eliminado correctamente.")
else:
    print("El producto no está en el inventario.")
    
print("Inventario final:", productos_vendidos)

