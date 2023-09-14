def PiWallis(n):
    i = 1
    p = 1
    while i <= n:
        if i % 2 == 0:
            numerador = i
            denominador = i + 1
        else:
            numerador = i + 1
            denominador = i
        p *= (numerador / denominador)
        i += 1
    
    return p * 2
    