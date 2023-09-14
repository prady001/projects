def extrai_nomes_de_usuarios(l):
    li = []
    for e in l:
        n = e.find('@')
        li.append(e[:n])
    return li

palavra = 'LuzAzul'
print(palavra[::-1])