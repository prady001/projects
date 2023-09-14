def calcula_total_da_nota(l1, l2):
    total = 0
    index = 0
    while index < len(l1):
        total += (l1[index] * l2[index])
        index += 1
    return total