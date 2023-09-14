import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import resolve_equacao_1o_grau
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'resolve_equacao_1o_grau')


gabarito_inteiros = [(2, 4, -2), (10, 0, 0), (1002, -1002, 1), (123, 246, -2), (3, -15, 5), (5000000000, -10000000000, 2)]

@pytest.mark.parametrize(
    'a, b, esperado',
    [pytest.param(a, b, esperado, id=f'a = {a}, b = {b}') for a, b, esperado in gabarito_inteiros]
)
def test_numeros_inteiros(a, b, esperado):
    obtido = resolve_equacao_1o_grau(a, b)
    assert obtido == esperado, f'Algo deu errado no cálculo para a = {a} e b = {b}.\nEra esperado {esperado}, mas foi obtido {obtido}.'


gabarito_decimais = [(4, 0.5, -0.125),(-8, 4.92, 0.615), (-0.15, 1, 6.666666666666667), (100, 22.5, -0.225), (-1000000, 456.87, 0.00045687), (567.9, 66.987, -0.11795562599049128)]

@pytest.mark.parametrize(
    'a, b, esperado',
    [pytest.param(a, b, esperado, id=f'a = {a}, b = {b}') for a, b, esperado in gabarito_decimais]
)
def test_numeros_decimais(a, b, esperado):
    obtido = resolve_equacao_1o_grau(a, b)
    assert obtido == pytest.approx(esperado), f'Algo deu errado no cálculo para a = {a} e b = {b}.\nEra esperado {esperado}, mas foi obtido {obtido}.'
