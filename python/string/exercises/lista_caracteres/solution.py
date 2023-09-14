def lista_caracteres(str):
    l = []
    for letra in str:
        if letra not in l:
            l.append(letra) 
    return l