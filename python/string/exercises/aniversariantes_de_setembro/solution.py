def aniversariantes_de_setembro(d1):
    # Inicializa um dicionário vazio para armazenar os aniversariantes de setembro.
    d2 = {}
    
    # Itera sobre os valores do dicionário de entrada "d1".
    for e in d1.values():
        # Verifica se o quinto caractere da segunda string na lista "e" é igual a '9' (setembro).
        if e[1][4] == '9':
            # Se for setembro, adiciona a primeira string como chave e a lista completa como valor em "d2".
            d2[e[0]] = e[1]
    
    # Retorna o dicionário "d2" com os aniversariantes de setembro.
    return d2
