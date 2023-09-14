from math import tan
def calcula_area_do_pentagono(l):
    t = tan(0.628319)
    area = (5 / 4) *  ((l ** 2) / t)
    return area

