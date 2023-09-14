from math import *
def entregador_mais_proximo(restaurante, entregadores):
    min = inf
    c = 0
    for j in entregadores:
        d = sqrt((j[0] - restaurante[0]) ** 2 + (j[1] - restaurante[1]) ** 2)
        if d < min:
            min = d
            k = c
        c += 1
    return k