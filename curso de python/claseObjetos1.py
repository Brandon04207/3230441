#esto es para crear una clase y objetos en python
#clase objetos
"clase de atributos estaticos"
class Celular():
    marca = "samsung"
    modelo = "s23"
    camara = "48mp"

#crear un objeto a partir de la clase    
celular1 = Celular()
print(celular1.marca)

#crear otro objeto a partir de la clase
"clase de atributos dinamicos de instancia"
class Celular2:
    #def es para definir un metodo o funcion dentro de una clase
    #__init_ es un metodo especial que se ejecuta automaticamente al crear un objeto a partir de la clase
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        #el self es para referirse al objeto que se esta creando a partir de la clase, y se utiliza para asignar valores a los atributos del objeto
    def llamar (self):
        print(f"estoy llamando desde un: {self.modelo}")
        
    def colgar (self):
        print(f"estoy colgando desde un: {self.modelo}")
        #__str__ es un metodo especial que se ejecuta automaticamente al imprimir un objeto a partir de la clase, y devuelve una cadena de texto con la informacion del objeto
    def __str__ (Self):
        return f"este celular es de la marca {Self.camara} y referencia {Self.modelo} y una camara {Self.camara}"
        
celular1=Celular2("samsung" , "s25" , "48mp")
celular2=Celular2("apple" , "iphone 17" , "48mp")
celular3=Celular2("huawei" , "P20" , "12mp")

#inprimir el modelo del celular1
print (celular1.modelo)
celular1.llamar()
celular1.colgar()
#impirme la informacion del celular1 utilizando el metodo __str__
print(celular1)