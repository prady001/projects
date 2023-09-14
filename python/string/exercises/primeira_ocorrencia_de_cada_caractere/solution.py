def primeiras_ocorrencias(str):
    d = {}
    count = 1
    for e in str:
        if e not in d:
            d[e] = str.find(e)
    return d