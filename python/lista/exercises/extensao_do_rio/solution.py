from math import *
def calcula_extensao(l1, l2):
    i = 0
    s = 0
    while i < len(l1) - 1:
        d1 = l1[i + 1] - l1[i]
        d2 = l2[i + 1] - l2[i]
        i += 1
        r = sqrt((d1 ** 2) + (d2 ** 2))
        s += r
    return s