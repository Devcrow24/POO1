from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcularArea():
        pass

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
       self.lado = lado
    
    def calcularArea(self):
        return self.lado * self.lado

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2
    
#---------------------------------------Iniciating programing
unTriangulo = Triangulo(4,6)
print(unTriangulo.calcularArea())

unCuadrado = Cuadrado(4)
print(unCuadrado.calcularArea())