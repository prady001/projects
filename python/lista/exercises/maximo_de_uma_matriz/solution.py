def encontra_maximo(l):
    i =  0
    j = 0
    maior = abs(l[i][j])
    j = 1
    while i < 3:
        while j < 3:
            if abs(l[i][j]) > maior:
                maior = abs(l[i][j])
            j += 1
        i += 1
        j = 0
    return maior