from math import radians, tan
class Figura:
    def area(nLados, vLado):
        if nLados > 0:
            angulo = radians(360 / (nLados * 2))
            apotema = vLado / (2 * (tan(angulo)))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
        return "El area de la figuranes", areaFigura

    def perimetro(nLados, vLado):
        perimetroFigura = vLado * nLados
        return "El perimetro de la figura es", perimetroFigura

#--------------------------------------------------------Iniciating programing
unaFigura = Figura
print(unaFigura.area(4,4))
print(unaFigura.perimetro(4,4))