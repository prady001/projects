def filtra_positivos(numbers):
    sum_pos = []
    for n in numbers:
        if n > 0:
            sum_pos.append(n)
    return sum_pos