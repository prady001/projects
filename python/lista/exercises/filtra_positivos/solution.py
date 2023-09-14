def filtra_positivos(l):
    positivos = []
    i = 0
    while i < len(l):
        if l[i] > 0:
            positivos.append(l[i])
        i += 1
    return positivos