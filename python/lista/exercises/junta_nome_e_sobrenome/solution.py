def nomes_completos(l1, l2):
    l3 = []
    index = 0
    while index < len(l1):
        l3.append(l1[index] + ' ' + (l2[index])) 
        index += 1
    return l3

