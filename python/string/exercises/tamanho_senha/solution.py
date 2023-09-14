def tamanho_minimo(str, n):
    
    l = []
    palavra = str.split()
    
    for e in palavra:
        if len(e) > n:
            l.append(e)

    return l

    