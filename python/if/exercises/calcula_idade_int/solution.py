def calcula_idade(d1, m1, a1, d2, m2, a2):
    if m2 > m1:
        return a2 - a1
    elif m2 < m1 and d2 > d1:
        return a2 - a1 - 1
    elif m2 < m1 and d2 < d1:
        return a2 - a1 - 1
    if m2 == m1 and d2 > d1:
        return a2 - a1
    elif m2 == m1 and d2 < d1:
        return a2 - a1 - 1
    elif m2 == m1 and d2 == d1:
        return a2 - a1 