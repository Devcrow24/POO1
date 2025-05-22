import math
class Figura:
    def area(numeroLados, valorLados):
        #Triangulo
        if numeroLados == 3:
            preH = (valorLados/2)**2 + valorLados**2
            h = math.sqrt(preH)
            b = valorLados
            areaFigura = (b*h)/2
            print("El area del triangulo es: ", areaFigura)

        #cuadrado
        if numeroLados == 4:
            b = valorLados
            h = valorLados
            areaFigura = b*h
            print("El area del cuadrado es: ", areaFigura)
        
        #poligono regular
        if numeroLados > 0:
            angulo = math.radians(360 / (numeroLados * 2))
            apotema = valorLados / (2 * (math.tan(angulo)))
            p = valorLados * numeroLados
            areaFigura = (p * apotema) / 2
            print("El area de la figura es: ", areaFigura)

    def perimetro(numeroLados, valorLados):
        if numeroLados == 3:
            perimetroFigura = valorLados * 3
            print("El perimetro del triangulo es: ", perimetroFigura)
        
        if numeroLados == 4:
            perimetroFigura = valorLados * 4
            print("El perimetro del cuadrado es: ", perimetroFigura)
        
        if numeroLados == 5:
            perimetroFigura = valorLados * 5
            print("El perimetro del pentagono es: ", perimetroFigura)

#--------------------------------------------------------
unaFigura = Figura
unaFigura.area(4,4)
unaFigura.perimetro(4,4)