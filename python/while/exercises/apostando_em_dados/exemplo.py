import random
from solution import apostando_em_dados

random.seed(1)
numero_da_sorte = 5
aposta = 180
rodadas = 3

print(apostando_em_dados(numero_da_sorte, aposta, rodadas))
# Deve imprimir:  166.66666666666669
