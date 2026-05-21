#una lista es una colección de elementos ordenados y mutables,
# que permite elementos duplicados. Las listas se definen con corchetes [] o con la función list().

lista = ["banano", "pera", "mora", "fresa", "kiwi"]
print (lista)
x= len (lista) #len() devuelve la cantidad de elementos en la lista.
print(lista[1]) # para acceder a un elemento de la lista, se utiliza el índice del elemento entre corchetes [].
print("--------------------------------------------------------")

lista [2] = "mango" 
print (lista) # modifica el elemento en el índice 2 de la lista, en este caso, "mora" se cambia por "mango".
print("--------------------------------------------------------")

lista[1:3] = ["naranja", "piña"]
print (lista) # modifica la pocicion 1 y 2 de la lista ya que no hay un elemento en la pocision 3 a modificar.
print("--------------------------------------------------------")

lista.insert(2, "papaya")
print (lista) # inserta el elemento "papaya" en la pocision 2 de la lista.
print("--------------------------------------------------------")

lista.append("maracuya")
print (lista) # agrega el elemento "maracuya" al final de la lista, solo un elemento se puede agregar con append().
print("--------------------------------------------------------")

lista2 = ["melon", "sandia"]
lista.extend(lista2)
print (lista) # agrega los elementos de lista2 al final de lista, se pueden agregar varios elementos con extend().
print("--------------------------------------------------------")

lista.remove("naranja")
print (lista) # elimina el primer elemento de la lista que coincida con el valor especificado, en este caso, "naranja", elimina el primer elemento que coincida.
print("--------------------------------------------------------")

lista.pop(3)
print (lista) # elimina el elemento en la pocision 3 de la lista, si no especifica elimina el ultimo elemento de la lista.
print("--------------------------------------------------------")

lista.sort()
print (lista) # ordena la lista en orden ascendente, es decir, de la A a la Z, o de menor a mayor si son números.
print("--------------------------------------------------------")

lista.sort(reverse=True)
print (lista) # ordena la lista en orden descendente, es decir, de la Z a la A, o de mayor a menor si son números.
print("--------------------------------------------------------")
