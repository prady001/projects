from math import sqrt
def calcula_pi(n):
    s = 0
    while n > 0:
        E = 6 / (n ** 2)
        s += E
        n -= 1
    return sqrt(s)