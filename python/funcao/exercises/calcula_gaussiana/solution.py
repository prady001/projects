from math import e, pi

def calcula_gaussiana(x, mu, sigma):
   A = 1 / (sigma * ((2 * pi) ** (1 / 2)))
   B = (-0.5) * ((((x - mu) / sigma)) ** 2)
   gaussiana = A * ((e) ** B)
   return gaussiana
