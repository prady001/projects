def calcula_total_da_nota(l1, l2):
    
    s = 0

    for index in range(len(l1)):
        p = l1[index] * l2[index]
        s += p

    return s







"""def nomes_completos(l1, l2):
    l3 = []
    for index in range(len(l1)):
        l3.append(l1[index] + ' ' + l2[index])
    return l3"""