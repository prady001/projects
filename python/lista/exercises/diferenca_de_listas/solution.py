def subtracao_de_listas(l1, l2):
    l3 = []
    for e in l1:
        if e not in l2:
            l3.append(e)
    return l3
