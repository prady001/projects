from math import e
import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import encontra_cateto
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'encontra_cateto')



gabarito_inteiros = [(3, 5, 4), (4, 5, 3), (6, 10, 8), (8, 10, 6), (7, 25, 24), (5, 13, 12), (15, 17, 8), (80, 100, 60), (323, 325, 36), (280, 325, 165)]

@pytest.mark.parametrize(
    'cateto, hipotenusa, esperado',
    [
        pytest.param(cateto, hipotenusa, esperado, id=f'cateto = {cateto}, hipotenusa = {hipotenusa}') for cateto, hipotenusa, esperado in gabarito_inteiros
    ]
)
def test_numeros_inteiros(cateto, hipotenusa, esperado):
    obtido = encontra_cateto(cateto, hipotenusa)
    assert obtido == esperado, f'Algo deu errado no cálculo do outro cateto.\nPara a hipotenusa {hipotenusa} e o cateto {cateto} era esperado {esperado}, mas foi obtido {obtido}.'


gabarito_decimais = [(52.492, 111.7654, 98.67165030118834), (4.25, 5.55, 3.569313659514949), (32.465, 47.825, 35.117722021794066), (100.2, 111.58, 49.09232526576837), (1.238, 6.762, 6.647706371373513)]

@pytest.mark.parametrize(
    'cateto, hipotenusa, esperado',
    [
        pytest.param(cateto, hipotenusa, esperado, id=f'cateto = {cateto}, hipotenusa = {hipotenusa}') for cateto, hipotenusa, esperado in gabarito_decimais
    ]
)
def test_numeros_decimais(cateto, hipotenusa, esperado):
    obtido = encontra_cateto(cateto, hipotenusa)
    assert obtido == esperado, f'Algo deu errado no cálculo do cateto para valores decimais.\nPara a hipotenusa {hipotenusa} e o cateto {cateto} era esperado {esperado}, mas foi obtido {obtido}.'


gabarito_altos = [(5000, 13000, 12000), (23067, 32045, 22244), (22244, 32045, 23067), (17253, 32045, 27004), (120000000, 130000000, 50000000)]

@pytest.mark.parametrize(
    'cateto, hipotenusa, esperado',
    [
        pytest.param(cateto, hipotenusa, esperado, id=f'cateto = {cateto}, hipotenusa = {hipotenusa}') for cateto, hipotenusa, esperado in gabarito_altos
    ]
)
def test_valores_altos(cateto, hipotenusa, esperado):
    obtido = encontra_cateto(cateto, hipotenusa)
    assert obtido == esperado, f'Algo deu errado no cálculo do outro cateto para valores mais altos.\nPara a hipotenusa {hipotenusa} e o cateto {cateto} era esperado {esperado}, mas foi obtido {obtido}.'
