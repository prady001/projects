import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import inverte_lista
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'inverte_lista')


@pytest.mark.timeout(5)
def test_lista_vazia():
    lista_original, lista_invertida = [], []
    resultado = inverte_lista(lista_original)
    assert resultado == lista_invertida, f'Algo deu errado na hora de inverter a lista {lista_original}.\nEra esperado {lista_invertida}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_de_1_elemento():
    lista_original, lista_invertida = ['único'], ['único']
    resultado = inverte_lista(lista_original)
    assert resultado == lista_invertida, f'Algo deu errado na hora de inverter a lista {lista_original}.\nEra esperado {lista_invertida}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_de_repetidos_nao_sequenciais():
    lista_original, lista_invertida = [1, 3, 2, 3, 4], [4, 3, 2, 3, 1]
    resultado = inverte_lista(lista_original)
    assert resultado == lista_invertida, f'Algo deu errado na hora de inverter a lista {lista_original}.\nEra esperado {lista_invertida}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_de_repetidos_sequenciais():
    lista_original, lista_invertida = [1, 3, 3, 3, 4], [4, 3, 3, 3, 1]
    resultado = inverte_lista(lista_original)
    assert resultado == lista_invertida, f'Algo deu errado na hora de inverter a lista {lista_original}.\nEra esperado {lista_invertida}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_de_palindromo():
    lista_original, lista_invertida = ['t', 'e', 'n', 'e', 't'], ['t', 'e', 'n', 'e', 't']
    resultado = inverte_lista(lista_original)
    assert resultado == lista_invertida, f'Algo deu errado na hora de inverter a lista {lista_original}.\nEra esperado {lista_invertida}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_de_strings():
    lista_original, lista_invertida = ['nolan', 'tdk', 'inception', 'interstellar'], ['interstellar', 'inception', 'tdk', 'nolan']
    resultado = inverte_lista(lista_original)
    assert resultado == lista_invertida, f'Algo deu errado na hora de inverter a lista {lista_original}.\nEra esperado {lista_invertida}, mas foi obtido {resultado}.'
