import math
class Figura:
    def area(nLados, vLado):
        if nLados > 0:
            angulo = math.radians(360 / (nLados * 2))
            apotema = vLado / (2 * (math.tan(angulo)))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
            print("El area de la figura es: ", areaFigura)

    def perimetro(nLados, vLado):
        perimetroFigura = vLado * nLados
        print("El perimetro del triangulo es: ", perimetroFigura)

#--------------------------------------------------------
unaFigura = Figura
unaFigura.area(4,4)
unaFigura.perimetro(4,4)