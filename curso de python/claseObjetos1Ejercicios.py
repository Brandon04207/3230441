nombre = input("ingrese el nombre del estudiante: ")
edad = input("ingrese la edad del estudiante: ")
grado = input("ingrese el grado del estudiante: ")


#la clase es una plantilla para crear objetos, es un conjunto de atributos y metodos que definen un tipo de objeto.
#la clase padre es la clase que se utiliza para crear objetos, es la clase que se utiliza para crear objetos de una clase hija.
class Estudiante ():
    def __init__(self,nombre,edad,grado):
            self.nombre = nombre
            self.edad = edad
            self.grado = grado
        
    def __str__ (self):
            return f"este estudiante se llama {self.nombre} y tiene {self.edad} años y esta estudiando {self.grado}"
    
Estudiante1= Estudiante(nombre, edad, grado)

    
print(Estudiante1)

while True:
    pregunta = input("usted esta estudiando? (si/no): ")
    if pregunta == "si":
        print(f"{nombre} sigue estudiando")
    else:
        break
    


    