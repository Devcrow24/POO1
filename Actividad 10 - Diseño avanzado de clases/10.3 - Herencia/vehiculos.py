from abc import ABC, abstractmethod, abstractproperty
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Electrico(ABC):
    @abstractmethod
    def cargar(self):
        pass

class CocheElectrico(Vehiculo, Electrico):
    def mover(self):
        return "Moviendo coche eléctrico"

    def cargar(self):
        return "Cargando batería"
    
#---------------------------------------Iniciating programing
unCarro = CocheElectrico()
print(unCarro.mover())
print(unCarro.cargar())