from math import *
def maximo_divisor_comum(n1, n2):
    i = 1
    maior = -inf
    l = []
    while i < n1 or i < n2:
        if n1 % i == 0 and n2 % i == 0:
            l.append(i)
        i += 1
    for e in l:
        if e > maior:
            maior = e
    return maior
r = maximo_divisor_comum(32, 79)
print(r) 
'''   j = max(n1, n2)
    maior = -inf
    while j > 0:
        if n1 % j == 0 and n2 % j == 0:
            maior = j
        j -= 1

    print(maior)'''