#decoradores 
#es otra funcion que recibe como parametro otra funcion y le agrega una funcionalidad extra a esa funcion sin modificar su codigo
def miDecorador(funcion):
    def envoltura():
        print ("antes de ejecutar la funcion")
        funcion()
        print("despues de ejecutar la funcion")
    return envoltura

@miDecorador
def saludar ():
    print("hola parcero")

saludar()