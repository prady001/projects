def raiz_quadrada(n):
    i = 1
    c = 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    while (n - i) > 0:
        sub = n - i
        n = sub
        c += 1
        i += 2
    return c 

r = raiz_quadrada(9)
print(r)