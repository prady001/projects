import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import libras_para_kg
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'libras_para_kg')


gabarito = [(0.265, 0.12020188000000001), (1, 0.453592), (5, 2.26796), (7.5, 3.4019399999999997), (25, 11.3398), (100, 45.3592), (122.55, 55.5876996), (24590000000, 11153827280)]

@pytest.mark.parametrize(
    'entrada, esperado',
    [pytest.param(i, j, id=f'libras={i}') for i, j in gabarito]
)
def test_pesos(entrada, esperado):
    obtido = libras_para_kg(entrada)
    assert obtido == pytest.approx(esperado), f'Algo deu errado para o peso {entrada} em libras.\nEra esperado {esperado} mas foi obtido {obtido}.'
