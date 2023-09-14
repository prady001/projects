from math import factorial

def calcula_euler(x, n):
    s = 0
    while n > 0:
        e = (x ** (n - 1)) / factorial(n - 1)
        s += e 
        n -= 1
    
    return s
