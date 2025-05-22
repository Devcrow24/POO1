#Abdiel Muñiz
#9/01/2025

import math
class Figura:
    def __init__(self, nLados, vLados):
        self.nLados = nLados
        self.vLados = vLados

    def calcularArea(self):
        #Triangulo
        if self.nLados == 3:
            preH = (self.vLados/2)**2 + self.vLados**2
            h = math.sqrt(preH)
            b = self.vLados
            areaFigura = (b*h)/2
            return "El area del triangulo es: ", areaFigura

        #cuadrado
        if self.nLados == 4:
            b = self.vLados
            h = self.vLados
            areaFigura = b*h
            return "El area del cuadrado es: ", areaFigura
        
        #poligono regular
        if self.nLados > 0:
            angulo = math.radians(360 / (self.nLados * 2))
            apotema = self.vLados / (2 * (math.tan(angulo)))
            p = self.vLados * self.nLados
            areaFigura = (p * apotema) / 2
            return "El area de la figura es: ", areaFigura

    def calcularPerimetro(self):
        #Triangulo
        if self.nLados == 3:
            perimetroFigura = self.vLados * 3
            return "El perimetro del triangulo es: ", perimetroFigura
        
        #Cuadrado
        if self.nLados == 4:
            perimetroFigura = self.vLados * 4
            return "El perimetro del cuadrado es: ", perimetroFigura
        
        #Pentagono
        if self.nLados == 5:
            perimetroFigura = self.vLados * 5
            return "El perimetro del pentagono es: ", perimetroFigura

#--------------------------------------------------------Iniciating programing
unaFigura = Figura(4,4)
print(unaFigura.calcularArea())
print(unaFigura.calcularPerimetro())