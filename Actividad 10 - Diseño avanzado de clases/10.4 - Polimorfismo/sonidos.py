class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "miau"

def hacer_sonidos(listaAnimal):
    for animal in listaAnimal:
        print(animal.nombre, "hace", animal.hacer_sonido())

#---------------------------------------Iniciating programing

animales = [Perro("Humbe"), Gato("Calamardo")]
hacer_sonidos(animales)