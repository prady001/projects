import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import junta_listas
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'junta_listas')


@pytest.mark.timeout(5)
def test_lista_do_exemplo():
    lista_bruta = [[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]]
    lista_filtrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = junta_listas(lista_bruta)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de obter a lista filtrada a partir de {lista_bruta}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_da_lista_da_lista():
    lista_bruta = [[[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]], [[1, 2, 3], [], [], [4, 5, 6], [7, 8], [9], [10]]]
    lista_filtrada = [[1, 2, 3], [4, 5, 6], [7, 8], [9], [10], [1, 2, 3], [], [], [4, 5, 6], [7, 8], [9], [10]]
    resultado = junta_listas(lista_bruta)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de obter a lista filtrada a partir de {lista_bruta}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_lista_vazia():
    lista_bruta = []
    lista_filtrada = []
    resultado = junta_listas(lista_bruta)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de obter a lista filtrada a partir de {lista_bruta}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'
