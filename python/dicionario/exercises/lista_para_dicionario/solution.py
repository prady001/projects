""" CÓDIGO RUIM
def monta_dicionario(chaves, valores):
    chaves = tuple(chaves)
    chaves = tuple(valores)
    dic = {}
    dic[chaves] = valores
    return dic"""

""" CÓDIGO FUNCIONAL
def monta_dicionario(lista_chaves, lista_valores):
        
    dicionario = dict(zip(lista_chaves, lista_valores))
    return dicionario"""

def monta_dicionario(chaves, valores):
       
    dic = {}
    for i in range(len(chaves)):
        dic[chaves[i]] = valores[i]
    
    return dic