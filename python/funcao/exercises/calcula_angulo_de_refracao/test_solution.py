import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import snell_descartes
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'snell_descartes')

@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'n1 = {entradas[0]}, n2 = {entradas[1]} e teta1 = {entradas[2]}')
    for entradas, esperado in [
        ((1.0003, 1.71, 37), 20.612398082211552),
        ((1.33, 1.36, 72), 68.44687227796945),
        ((1.46, 2.42, 45), 25.252082399158706),
    ]
])
def test_valores_de_ângulo_positivos(entradas, esperado):
    obtido = snell_descartes(entradas[0], entradas[1], entradas[2])
    assert obtido == pytest.approx(
        esperado), f"Algo deu errado ao testar os valores de n1={entradas[0]}, n2={entradas[1]} e teta1={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'n1 = {entradas[0]}, n2 = {entradas[1]} e teta1 = {entradas[2]}')
    for entradas, esperado in [
        ((1.71, 2.42, -20), -13.98544438308455),
        ((1.31, 1.46, -55), -47.30658977780668),
        ((1.71, 1.33, -10), -12.900695166315176),
    ]
])
def test_valores_de_ângulos_negativos(entradas, esperado):
    obtido = snell_descartes(entradas[0], entradas[1], entradas[2])
    assert obtido == pytest.approx(
        esperado), f"Algo deu errado ao testar os valores de n1={entradas[0]}, n2={entradas[1]} e teta1={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."
