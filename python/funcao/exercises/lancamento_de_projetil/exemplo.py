import math
from solution import calcula_distancia_do_projetil

velocidade = 20
angulo = math.pi/4
altura = 1

resultado = calcula_distancia_do_projetil(velocidade, angulo, altura)
print(resultado)  # Deve imprimir aproximadamente 41.792958199885284
