from primo import eh_primo, primos_entre
from math import *


def maior_primo_menor_que(n):
    maior = -inf
    if not eh_primo(n) and n <= 0 or n == 1:
        return -1
    else:
        primo = primos_entre(1, n)
        for e in primo:
            if e > maior:
                maior = e
        return maior
