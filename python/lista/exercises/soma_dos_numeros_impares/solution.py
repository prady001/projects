def soma_impares(l):
    index = 0
    soma_impar = 0

    while index < len(l):
        if l[index] % 2 != 0:
            soma_impar += l[index]
        index += 1
    return soma_impar