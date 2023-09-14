"""def inverte_dicionario(d1):
    d2 = {}
    for nome, idade in d1.items():
        d2[idade] = nome
    return d2"""

def inverte_dicionario(dicionario):
    dicionario_invertido = {}
    
    # Itera sobre o dicionário original
    for nome, idade in dicionario.items():
        # Verifica se a idade já está no dicionário invertido
        if idade in dicionario_invertido:
            # Se sim, adiciona o nome à lista existente
            dicionario_invertido[idade].append(nome)
        else:
            # Se não, cria uma nova lista com o nome
            dicionario_invertido[idade] = [nome]
    
    return dicionario_invertido