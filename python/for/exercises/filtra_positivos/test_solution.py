import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import filtra_positivos
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'filtra_positivos')



def test_lista_vazia():
    lista_original, lista_filtrada = [], []
    resultado = filtra_positivos(lista_original)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de filtrar somente os números positivos de {lista_original}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'


def test_lista_nula():
    lista_original, lista_filtrada = [0], []
    resultado = filtra_positivos(lista_original)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de filtrar somente os números positivos de {lista_original}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'


def test_lista_positiva():
    lista_original, lista_filtrada = [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]
    resultado = filtra_positivos(lista_original)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de filtrar somente os números positivos de {lista_original}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'


def test_lista_negativa():
    lista_original, lista_filtrada = [-1,-2,-3,-4,-5,-6,-7,-8,-9], []
    resultado = filtra_positivos(lista_original)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de filtrar somente os números positivos de {lista_original}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'


def test_lista_nula_negativa_positiva():
    lista_original, lista_filtrada = [-1, -2, -3, 0, 1, 2], [1, 2]
    resultado = filtra_positivos(lista_original)
    assert resultado == lista_filtrada, f'Algo deu errado na hora de filtrar somente os números positivos de {lista_original}.\nEra esperado {lista_filtrada}, mas foi obtido {resultado}.'
