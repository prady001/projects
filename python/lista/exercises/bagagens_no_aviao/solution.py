def filtra_bagagens(bagagens, altura, largura, profundidade):
    c = 0
    i = 0
    '''for e in bagagens[e]:
        if (bagagens[e] > 55) or (bagagens[e + 1] > 35) or (bagagens[e + 2] > 25):
            c += 1
    return c'''
    for e in bagagens:
        if (e[0] > altura) or (e[1] > largura) or (e[2] > profundidade):
            c += 1

    return c