from solution import traduz


lista_ingles = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']
dicionario_ingles_port = {
    'pineapple': 'abacaxi',
    'plum': 'ameixa',
    'blackberry': 'amora',
    'apple': 'maçã',
    'cashew': 'caju',
    'cherry': 'cereja'
}
resultado = traduz(lista_ingles, dicionario_ingles_port)
# Esperado como resposta a lista: ['amora', 'cereja', 'ameixa', 'maçã', 'abacaxi']
print(resultado)
