from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import conta_ocorrencias
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'conta_ocorrencias')


def test_lista_vazia():
    entrada = []
    obtido = conta_ocorrencias(entrada)
    esperado = {}
    assert obtido == esperado, f'Algo deu errado na contagem de listas vazias.\nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_palavras_iguais():
    entrada = ['pimenta', 'pimenta', 'pimenta', 'pimenta', 'pimenta', 'pimenta']
    obtido = conta_ocorrencias(entrada)
    esperado = {'pimenta': 6}
    assert obtido == esperado, f'Algo deu errado na contagem de listas de palavras iguais.\nPara a entrada {entrada} era esperado {esperado}, mas foi obtido {obtido}.'


def test_palavras_diferentes():
    entrada = ['banana', 'pimenta', 'arroz', 'acucar', 'laranja', 'cravo']
    obtido = conta_ocorrencias(entrada)
    esperado = {'banana': 1, 'pimenta': 1, 'arroz': 1, 'acucar': 1, 'laranja': 1, 'cravo': 1}
    assert obtido == esperado, f'Algo deu errado na contagem de listas sem repetições de palavras.\nPara a entrada {entrada} era esperado {esperado}, mas foi obtido {obtido}.'


def test_uma_palavra():
    entrada = ['banana'] 
    obtido = conta_ocorrencias(entrada)
    esperado = {'banana': 1}
    assert obtido == esperado, f'Algo deu errado na contagem de listas com apenas uma palavra.\nPara a entrada {entrada} era esperado {esperado}, mas foi obtido {obtido}.'


def test_lista_com_repeticoes():
    entrada = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu', 'cravo']
    obtido = conta_ocorrencias(entrada)
    esperado = {'abobora': 3, 'chuchu': 2, 'cravo': 1}
    assert obtido == esperado, f'Algo deu errado na contagem com listas sem repetições de palavras.\nPara a entrada {entrada} era esperado {esperado}, mas foi obtido {obtido}.'
