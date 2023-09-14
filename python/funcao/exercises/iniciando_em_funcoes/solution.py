import math

# Função que converte graus em radianos
def graus_para_radianos(graus):
    rad = graus * ((math.pi) / 180)
    return rad

print(math.cos((math.pi) / 6))
print(math.cos((2 * (math.pi)) / 3))

rad30 = graus_para_radianos(30)
print(math.cos(rad30))
rad120 = graus_para_radianos(120)
print(math.cos(rad120))