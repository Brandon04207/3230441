#polimorfismo
class animal:
    def hablar(self):
        #NotImplementedError es un error que se lanza cuando se llama a un metodo que no ha sido implementado por la subclase
        #raise obliga que todos los hijos de animal implementen el metodo hablar, si no lo hacen, se lanzara un error.
        raise NotImplementedError("este metodo debe ser implementado por la subclase")

class perro(animal):
    def hablar (self):
        return "wow"
    
class gato(animal):
    def hablar (self):
        return "maiu"

class vaca(animal):
    def hablar (self):
        return "muu"
    
#lista de animales
animales= [perro(), gato(), vaca()]

#for para recorrer la lista de animales y llamar al metodo hablar de cada animal
for animal in animales:
    print(animal.hablar())