def aproxima_raiz(n):
    if n < 0:
        return None  # Não é possível calcular a raiz de um número negativo
    
    if n <= 1:
        return n  # A raiz quadrada de 0 ou 1 é igual a eles mesmos

    i = 1
    while i * i <= n:
        i += 1

    # Verificando qual valor é mais próximo da raiz de n
    diff1 = n - (i - 1) * (i - 1)
    diff2 = i * i - n

    if diff1 < diff2:
        return i - 1
    else:
        return i


