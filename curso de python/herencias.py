class Persona: 
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar (self):
        return "hola estoy hablando"
    
class Empleado (Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #super es cuando lo sacamos del constructor de la clase padre para usarlo en la clase hija
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        return "hola estoy trabajando"
    
class Estudiante:
    def __init__(self, materia): 
        self.materia = materia
            
class EmpleadoEstudiante (Persona, Estudiante): 
    def __init__(self, nombre, edad, nacionalidad, materia, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Estudiante.__init__(self, materia)
            
        self.trabajo = trabajo
        self.salario = salario
        
santiago = EmpleadoEstudiante ("santiago", 25, "colombia", "matematicas","instructor", 600 )
print(santiago.hablar())