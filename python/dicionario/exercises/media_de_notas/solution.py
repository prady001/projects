def calcula_media(l):
    s = 0
    c = 0
    for elementos in l:
        for i in elementos.values():
            s += i
            c += 1
    media = s / c
    return media