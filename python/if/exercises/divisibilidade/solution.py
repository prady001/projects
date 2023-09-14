def divisivel(n):
    if n % 2 == 0 and n % 3 != 0:
        return 'Ins'
    if n % 3 == 0 and n % 2 != 0:
        return 'per'
    if n % 2 == 0 and n % 3 == 0:
        return 'Insper'
    else:
        return n