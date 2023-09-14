def alunos_impares(l):
    l_impares = []
    for i in range(len(l) - 1):
        if i % 2 != 0:
            l_impares.append(l[i])
    return l_impares