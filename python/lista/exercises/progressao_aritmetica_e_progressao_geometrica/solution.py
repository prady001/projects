# Definindo a função verifica_progressao que recebe uma lista como parâmetro
def verifica_progressao(lista):
    # Se a lista tiver menos de 2 elementos, retorna "NA"
    if len(lista) < 2:
        return "NA"
    # Calcula a razão da progressão aritmética (PA) como a diferença entre o segundo e o primeiro elemento
    razao_pa = lista[1] - lista[0]
    # Verifica se todos os elementos consecutivos na lista têm a mesma diferença (razao_pa)
    is_pa = all((lista[i+1] - lista[i] == razao_pa for i in range(len(lista)-1)))
    # Se o primeiro elemento da lista for zero, não é possível ter uma progressão geométrica (PG), então define is_pg como False
    if lista[0] == 0:
        is_pg = all((lista[i] == 0 for i in range(len(lista))))
        is_pg = False
    else:
        # Calcula a razão da progressão geométrica (PG) como a divisão do segundo pelo primeiro elemento
        razao_pg = lista[1] / lista[0]
        # Verifica se todos os elementos consecutivos na lista têm a mesma razão (razao_pg)
        is_pg = all((lista[i+1] / lista[i] == razao_pg for i in range(len(lista)-1)))
    
    # Se a lista é tanto PA quanto PG, retorna "AG"
    if is_pa and is_pg:
        return "AG"
    # Se a lista é PA, retorna "PA"
    elif is_pa:
        return "PA"
    # Se a lista é PG, retorna "PG"
    elif is_pg:
        return "PG"
    # Se a lista não é nem PA nem PG, retorna "NA"
    else:
        return "NA"
# Definindo a função verifica_progressao que recebe uma lista como parâmetro
