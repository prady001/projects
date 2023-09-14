def eh_crescente(l):
    
    for i in range(1, len(l)):
        if l[i] <= l[i - 1]:
            return False
    return True
