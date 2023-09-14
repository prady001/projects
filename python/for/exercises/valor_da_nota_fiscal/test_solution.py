import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_total_da_nota
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_total_da_nota')


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(([12, 1, 4, 6, 100, 43, 8], [1, 4, 6, 86, 5, 2, 77]), 1758,
                 id=f'precos=[12,1,4,6,100,43,8], quantidades=[1,4,6,86,5,2,77]'),
    pytest.param(([10, 145, 1, 45, 40], [15, 43, 7, 26, 5]), 7762,
                 id=f'precos=[10,145,1,45,40], quantidades=[15,43,7,26,5]'),
    pytest.param(([16, 13, 91, 52, 50, 33, 18, 71, 93, 245], [3, 5, 3, 4, 12, 18, 13, 60, 9, 20]),
                 12019, id=f'precos=[16,13,91,52,50,33,18,71,93,245], quantidades=[3,5,3,4,12,18,13,60,9,20]')
])
def test_precos_inteiros(entradas, esperado):
    obtido = calcula_total_da_nota(entradas[0], entradas[1])
    mensagem = f"Algo deu errado com ao processar preços inteiros, o esperado era: {esperado} e o obtido foi: {obtido}"
    assert obtido == esperado, mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(([1.21, 1.1, 4.5, 6.1, 100.15, 0.4, 8.67], [13, 41, 63, 6, 52, 14, 47]), 6001.82,
                 id=f'precos=[1.21,1.1,4.5,6.1,100.15,0.4,8.67], quantidades=[13,41,63,6,52,14,47]'),
    pytest.param(([1.40, 1.45, 11.4], [1, 63, 73]), 924.95,
                 id=f'precos=[1.40,1.45,11.4], quantidades=[1,63,73]'),
    pytest.param(([16.13, 9.12, 50.2, 33.42, 18.01, 71.1, 93.34, 245.33, 67.43, 86.7], [6, 1, 443, 42, 11, 38, 43, 61, 93, 1]),
                 51984.49, id=f'precos=[16.13,9.12,50.2,33.42,18.01,71.1,93.34,245.33,67.43,86.7], quantidades=[6,1,443,42,11,38,43,61,93,1')
])
def test_precos_decimais(entradas, esperado):
    obtido = calcula_total_da_nota(entradas[0], entradas[1])
    mensagem = f"Algo deu errado com ao processar preços decimais, o esperado era: {esperado} e o obtido foi: {obtido}"
    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(([2], [13]), 26, id=f'precos=[2], quantidades=[13]'),
    pytest.param(([1.40], [32]), 44.8, id=f'precos=[1.40], quantidades=[32]'),
    pytest.param(([1632], [122]), 199104,
                 id=f'precos=[1632], quantidades=[122]')
])
def test_lista_unitaria(entradas, esperado):
    obtido = calcula_total_da_nota(entradas[0], entradas[1])
    mensagem = f"Algo deu errado com listas de preços unitárias, o esperado era: {esperado} e o obtido foi: {obtido}"
    assert obtido == esperado, mensagem


def test_lista_vazia():
    obtido = calcula_total_da_nota([], [])
    esperado = 0
    mensagem = f"Algo deu errado com listas vazias, o esperado era: {esperado} e o obtido foi: {obtido}"
    assert obtido == esperado, mensagem
