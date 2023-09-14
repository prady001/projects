def calcula_serie(a, b, n):
    s = 0
    i = 0
    
    while i < n:
        e = 1 / (a ** (i * b))
        s += e
        i += 1
        return e
        print(e)

