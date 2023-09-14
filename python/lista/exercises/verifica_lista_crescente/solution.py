def eh_crescente(l):
    i = 0 
    while i < len(l) - 1:
        if l[i] < l[i + 1]:
            i += 1
        else:
            return False
    return True
        