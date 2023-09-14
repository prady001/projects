def conta_ocorrencias(lista_palavras):
    dic = {}


    

    for palavra in lista_palavras:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1

    return dic

