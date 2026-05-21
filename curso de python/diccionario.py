#diccionario es una estructura de datos que almacena pares de clave-valor,
# donde cada clave es única y se utiliza para acceder a su valor correspondiente. 
# Los diccionarios son mutables, lo que significa que puedes modificar sus elementos después de haberlos creado. 
# Se definen utilizando llaves {} y los pares de clave-valor se separan por comas.

diccionario={"nota1":5,"nota2":3.5,"nota3":[1,2,3] }
#aqui estamos creando un diccionario con tres pares de clave-valor, 
#!donde "nota1" es la clave y 5 es su valor, "nota2" es la clave y 3.5 es su valor, y "nota3" es la clave y [1,2,3] es su valor.

diccionario["nota3"]= [1,2,3]
#!aqui estamos modificando el valor de la clave "nota3" en el diccionario, asignándole una nueva lista [1,2,3].
print(diccionario["nota3"])

#!para acceder a un valor en el diccionario, se utiliza la clave entre corchetes [] o con el método get().
print("--------------------------------------------------------")

diccionario["nota3"]= [3,2,1,5,7]
print(diccionario["nota3"][1])

for key in diccionario:
    print(key,":",diccionario[key])
    print(key,":",diccionario.get(key))
    #!key es la variable que representa cada clave en el diccionario, 
    #! y diccionario[key] o diccionario.get(key) se utilizan para acceder al valor correspondiente a esa clave.
    
    
print("--------------------------------------------------------")
diccionario_Autos = {
    "Marca": "Ford",
    "Modelo": "Mustang",
    "Año": 1964}
print(diccionario_Autos)

diccionario_Autos["color"] = "red"
#!aqui estamos agregando un nuevo par de clave-valor al diccionario_Autos, donde "color" es la nueva clave y "red" es su valor.
print(diccionario_Autos)

print("--------------------------------------------------------")




diccionario_maquillaje ={
    "tipo_de_producto": input(" introduce el tipo de producto que deseas"),
    "color": input("introduce el tipo de tono o color "),
    "cantidad" : int(input("introduce la cantidad de productos que desas"))
    #!aqui estamos creando un diccionario llamado diccionario_maquillaje,
    #! donde cada clave se asigna a un valor ingresado por el usuario a través de la función input().
}
print(diccionario_maquillaje)

print("--------------------------------------------------------")


#1. Realizar una función que, dadas 5 de notas de cursos digitados por el
#usuario, se guarden en un diccionario:

#Ejemplo:{‘Algebra’:5 , ‘Fisica’:4}

def guardarNotas():
#? definimos una funcion llamada guardarNotas que no recibe ningun parametro.
    
    cursos= {}
    for i in range(5):
        nombre = input(f"ingrese el nombre del curso #{i+1}:")
        nota =float(input(f"ingrese la nota de {nombre}:"))
    #? hacemos un ciclo for que se repetira 5 veces, donde se le pide al usuario que ingrese el nombre del curso y la nota correspondiente,
    #? y se almacenan en las variables nombre y nota respectivamente.
        
        cursos[nombre] = nota
    #? aqui estamos agregando un nuevo par de clave-valor al diccionario cursos, donde nombre es la clave y nota es su valor.
        
    return cursos 

def main():
    notas = guardarNotas()
    print("el diccionario de notas es:", notas)
        
#? aqui estamos definiendo una funcion main que llama a la funcion guardarNotas para obtener el diccionario de notas ingresadas por el usuario,
#? y luego imprime cada curso y su nota correspondiente utilizando un ciclo for que itera sobre los elementos del diccionario con el metodo items().