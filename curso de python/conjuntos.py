conjunto = {"manzana","banano","uva"}
#un conjunto es una colección de elementos únicos, no permite elementos duplicados, no tiene un orden específico y es mutable.
#los conjuntos se definen con llaves {} o con la función set().
for x in conjunto:
    print(x)
print ("pera" in conjunto)
print ("banano" in conjunto)

#agregar elemento al conjunto

conjunto.add("naranja")

print(conjunto)

conjunto2 = {"piña", "mango", "papaya"}

conjunto.update (conjunto2)
print (conjunto)

#remove elimina conjunto, tira error, con el discard no tira error 

conjunto.discard("borojo")
print (conjunto)

#pop(), elimina un elemento de ese conjunto aleatoriamente 

conjunto.pop()
print (conjunto)

#clear deja vacia el conjunto

#del elimina el conjunto completo 

#set() es para crear un conjunto vacio, si se crea un conjunto con set() y se le agrega un elemento, el conjunto ya no estara vacio.

#len() devuelve la cantidad de elementos únicos en el conjunto numeros.

print("---------------------------------------------------------------------------------------------------------------")

# || para unir conjuntos, & para la intersección (osea los elementos que están en ambos conjuntos)
# - para la diferencia(osea los elementos que están en el primer conjunto pero no en el segundo), ^ para la diferencia simétrica.

ejemplo1 = {1,2,3,4,5}
ejemplo2 = {4,5,6,7,8} 

print("unión: ", ejemplo1 | ejemplo2)
print("intersección: ", ejemplo1 & ejemplo2)
print("diferencia: ", ejemplo1 - ejemplo2)
print("diferencia simétrica: ", ejemplo1 ^ ejemplo2)


