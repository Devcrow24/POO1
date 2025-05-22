#Abdiel Muñiz
#9/01/2025

import math
class Figura:
    def area(nLados, vLados):
        #Triangulo
        if nLados == 3:
            preH = (vLados/2)**2 + vLados**2
            h = math.sqrt(preH)
            b = vLados
            areaFigura = (b*h)/2
            return "El area del triangulo es: ", areaFigura

        #cuadrado
        if nLados == 4:
            b = vLados
            h = vLados
            areaFigura = b*h
            return "El area del cuadrado es: ", areaFigura
        
        #poligono regular
        if nLados > 0:
            angulo = math.radians(360 / (nLados * 2))
            apotema = vLados / (2 * (math.tan(angulo)))
            p = vLados * nLados
            areaFigura = (p * apotema) / 2
            return "El area de la figura es: ", areaFigura

    def perimetro(nLados, vLados):
        #Triangulo
        if nLados == 3:
            perimetroFigura = vLados * 3
            return "El perimetro del triangulo es: ", perimetroFigura
        
        #Cuadrado
        if nLados == 4:
            perimetroFigura = vLados * 4
            return "El perimetro del cuadrado es: ", perimetroFigura
        
        #Pentagono
        if nLados == 5:
            perimetroFigura = vLados * 5
            return "El perimetro del pentagono es: ", perimetroFigura

#--------------------------------------------------------Iniciating programing
unaFigura = Figura
print(unaFigura.area(4,4))
print(unaFigura.perimetro(4,4))