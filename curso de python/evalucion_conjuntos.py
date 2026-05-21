usuariosActivos = set()
usuariosBloqueados = set()
usuariosAdministradores = set()

for i in range(6):
    nombre = input(f"ingrese el nombre del usuario activo {i+1}: ")
    usuariosActivos.add(nombre)

bloqueados= int(input("ingrese la cantidad de usuarios bloqueados: "))
for i in range(bloqueados):
    nombreBloqueado = input(f"a cual usuario desea bloquear: ")
    if nombreBloqueado in usuariosActivos:
        #in para verificar si el usuario bloqueado es un administrador,
        #si es así, se agrega a ambos conjuntos, si no, solo se agrega al conjunto de bloqueados.
        
        usuariosBloqueados.add(nombreBloqueado)
    else:
        print("el usuario no existe en el sistema")
        
administradores = int(input("ingrese la cantidad de usuarios administradores: "))
for i in range(administradores):
    nombreAdministrador = input(f"ingrese el nombre del usuario administrador {i+1}: ")
    if nombreAdministrador in usuariosActivos:
        usuariosAdministradores.add(nombreAdministrador)
    else:
        print("el usuario no existe en el sistema")
        
print("usuarios activos que no están bloqueados: ", usuariosActivos - usuariosBloqueados)
print("administradores que están bloqueados: ", usuariosAdministradores & usuariosBloqueados)
print("usuarios que no pertenecen a ningún grupo: ", usuariosActivos - (usuariosBloqueados | usuariosAdministradores))
print("---------------------------------------------------------------")

#------------------------------------------------------------------------


numerosPares = set()
numerosImpares = set()
while True:
    numero = input("Ingrese un número o 'fin' para terminar: ")
    if numero.lower() == "fin":
        print ("los numeros pares son",numerosPares)
        print ("los numeros impares son",numerosImpares)
        break
        
    elif numero():
        numero = int(numero)
        if numero % 2 == 0:
            numerosPares.add(numero)
        else:
            numerosImpares.add(numero)
    else:
        print("Entrada no válida. Por favor, ingrese un número o 'fin' para terminar.")

print("---------------------------------------------------------------")
#-------------------------------------------------------------- 
usuariosActorizados = set()

for i in range(5):
    nombre = input(f"ingrese el nombre del usuario autorizado {i+1}: ")
    usuariosActorizados.add(nombre)
print("---------------------------------------------------------------")
    
print("Acceso al sistema")  
    
for i in range(4):   
    nombreUsuario = input("Ingrese su nombre de usuario: ") 
    if nombreUsuario in usuariosActorizados:
        print("Acceso concedido")    
        break
    else:
        print("Acceso denegado, tieneste quedan", 2 - i, "intentos")

