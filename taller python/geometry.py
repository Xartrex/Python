'''En este ejemplo importaremos la clase math para calcular area y perimetro de
poligonos regulares'''

import math


print(dir(math))

class geometry():

    def __init__(self, x, y):
        self.long_lado = x
        self.num_lados = y

    def area(a):
        # sin(alfa) / a  =  sin(beta) * b   b = apotema
        alfa = float(math.pi /a.num_lados)
        beta = float(math.pi/2 - alfa)
        apotema = float(math.sin(beta)) / float(math.sin(alfa)) * float(a.long_lado) / float(2)
        area = float(a.long_lado) * apotema / 2 * float(a.num_lados)
        return area

    def perimetro(x):
        p = x.num_lados * x.long_lado
        return p

cmd = float(input("Introduce el numero de lados: "))
cmd2 = float(input("Introduce la longitud del lado: "))
polygon = geometry(cmd2, cmd)
print("El perimetro es " + str(polygon.perimetro()))
print("El area es " + str(polygon.area()))
