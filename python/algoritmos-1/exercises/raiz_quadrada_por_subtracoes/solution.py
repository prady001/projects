'''def raiz_quadrada(n):
    i = 1
    c = 0
    sub = True

    while sub > 0:
        sub = n - i
        n = sub
        c += 1
        i += 2
    
    return c'''

def raiz_quadrada(n):
    i = 1
    if n == 1:
        print(0)
    else:
        while i < n + 1:
            print(i)
            i += 2

r = raiz_quadrada(10)

