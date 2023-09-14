def conta_bigramas(s):
    d = {}  # Inicia um dicionário vazio para armazenar os bigramas e suas contagens
    i = 0   # Inicia um índice i para percorrer a string
    c = 1   # Inicia uma variável c para contar a frequência dos bigramas

    # Enquanto o índice i for menor que o comprimento da string - 1 (para evitar acessar um índice fora dos limites):
    while i < len(s) - 1:
        # Extrai o bigrama atual, que consiste em dois caracteres consecutivos
        bigrama = s[i:i + 2]
        
        # Verifica se o bigrama já está no dicionário
        if bigrama not in d:
            # Se não estiver, adiciona-o ao dicionário com contagem inicial de 1
            d[bigrama] = c
        else:
            # Se o bigrama já existe, incrementa sua contagem
            d[bigrama] += 1

        # Incrementa o índice para analisar o próximo bigrama na próxima iteração
        i += 1

    # Retorna o dicionário com os bigramas e suas contagens
    return d