from math import radians, tan
class Figura:
    def area(nLados, vLado):
        if nLados > 0:
            angulo = radians(360 / (nLados * 2))
            apotema = vLado / (2 * (tan(angulo)))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
        return areaFigura

    def perimetro(nLados, vLado):
        perimetroFigura = vLado * nLados
        return perimetroFigura
    
    def mostrarResultados():
        print("El area de la figura es: ", area())
        print("El perimetro de la figura es: ", perimetro())

#--------------------------------------------------------
unaFigura = Figura
unaFigura.area(4,4)
unaFigura.perimetro(4,4)
unaFigura.mostrarResultados()