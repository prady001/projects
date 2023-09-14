from pprint import pformat
import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import separa_trios
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'separa_trios')


entradas = [
    ['Jorge', 'Mariana'],
    ['João', 'Maria', 'Tiago'],
    ['Giovana', 'Beatriz', 'Lucas', 'Pedro'],
    ['João', 'Maria', 'Tiago', 'Pedro', 'Julia', 'Laura', 'Alice'],
    ['Adriana', 'Guilherme', 'Julia', 'Gabriel', 'Andre', 'Camila', 'Alice', 'Cida', 'Emilia', 'Evandro', 'Ana', 'Olivia', 'Felipe']
]

esperados = [
    [['Jorge', 'Mariana']],
    [['João', 'Maria', 'Tiago']],
    [['Giovana', 'Beatriz', 'Lucas'], ['Pedro']],
    [['João', 'Maria', 'Tiago'], ['Pedro', 'Julia', 'Laura'], ['Alice']],
    [['Adriana', 'Guilherme', 'Julia'], ['Gabriel', 'Andre', 'Camila'], ['Alice', 'Cida', 'Emilia'], ['Evandro', 'Ana', 'Olivia'], ['Felipe']]
]

@pytest.mark.parametrize(
    'entrada, esperado',
    [pytest.param(i, j, id=f'entrada={i}') for i, j in zip(entradas, esperados)]
)
def test_trios(entrada, esperado):
    obtido = separa_trios(entrada)
    assert obtido == esperado, f'Algo deu errado para a lista\n{pformat(entrada)}\n\nEra esperado\n{pformat(esperado)}\nmas foi obtido\n{pformat(obtido)}'


def test_lista_vazia():
    entrada = []
    esperado = []
    obtido = separa_trios(entrada)
    assert obtido == esperado, f'Algo deu errado para listas vazias.\nEra esperado {esperado}, mas foi obtido {obtido}.'
