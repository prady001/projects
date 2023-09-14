def inverte_lista(l1):
    l2 = []
    i = len(l1)
    x = len(l1) - 1
    while i > 0:
        l2.append(l1[x])
        i -= 1
        x -= 1
    l1 = l2
    return l1