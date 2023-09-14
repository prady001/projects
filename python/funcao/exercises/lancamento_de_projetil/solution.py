from math import sin
theta = '\u03B8'
g = 9.8
def calcula_distancia_do_projetil(v, theta, y0 ):
    d = ((v ** 2) / (2 * g)) * (1 + (1 + ((2 * g * y0) / ((v ** 2) * ((sin(theta) ** 2))))) ** (1/2)) * sin(2 * theta)
    return d