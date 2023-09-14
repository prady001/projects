def separa_trios(lista_de_alunos):
    trios = []  # Inicializa uma lista vazia para armazenar os trios
    i = 0  # Inicializa uma variável de índice

    # Enquanto o índice 'i' for menor que o tamanho da lista de alunos
    while i < len(lista_de_alunos):
        trio = lista_de_alunos[i:i + 3]  # Cria uma sublista de até 3 alunos
        trios.append(trio)  # Adiciona o trio à lista de trios
        i += 3  # Incrementa o índice em 3 para avançar para o próximo trio

    return trios  # Retorna a lista de trios
