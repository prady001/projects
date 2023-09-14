def conta_letras(str):
    d = {}
    count = 1
    for e in str:
        if e in d:
            d[e] += 1
        if e not in d:
            d[e] = count
    return d