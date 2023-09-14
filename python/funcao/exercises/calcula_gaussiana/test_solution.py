import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_gaussiana
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_gaussiana')



@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'x = {entradas[0]}, mi = {entradas[1]} e sigma = {entradas[2]}')
    for entradas, esperado in [
        ((3, 5, 7), 0.0547123942777446),
        ((1000, 621, 3049), 0.00012983669307222736),
        ((10000, 50000, 70000), 4.840684796525537e-06),
    ]
])
def test_valores_inteiros_positivos(entradas, esperado):
    obtido = calcula_gaussiana(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de x={entradas[0]}, mi={entradas[1]} e sigma={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."

    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'x = {entradas[0]}, mi = {entradas[1]} e sigma = {entradas[2]}')
    for entradas, esperado in [
        ((-1000, -621, -3049), -0.00012983669307222736),
        ((-10000, 50000, -70000), -3.947074079064297e-06),
        ((-1000, -621, 3049), 0.00012983669307222736),
        ((-10000, 50000, 70000), 3.947074079064297e-06),
        ((10000, -50000, 70000), 3.947074079064297e-06),
        ((10000, 50000, -70000), -4.840684796525537e-06)
    ]
])
def test_valores_inteiros_negativos(entradas, esperado):
    obtido = calcula_gaussiana(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de x={entradas[0]}, mi={entradas[1]} e sigma={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."
    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'x = {entradas[0]}, mi = {entradas[1]} e sigma = {entradas[2]}')
    for entradas, esperado in [
        ((3.56, 5.56, 7.78), 0.04961127205734614),
        ((1000.12, 621.86, 3049.97), 0.00012979994758349658),
        ((10000.75, 50000.86, 70000.964), 4.840635554574352e-06)
    ]
])
def test_valores_decimais_positivos(entradas, esperado):
    obtido = calcula_gaussiana(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de x={entradas[0]}, mi={entradas[1]} e sigma={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."
    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'x = {entradas[0]}, mi = {entradas[1]} e sigma = {entradas[2]}')
    for entradas, esperado in [
        ((-1000.45, -621.56, -3049.43), -0.00012981924956001248),
        ((-10000.32, 50000.77, -70000.23), -3.947017957205352e-06),
        ((-1000.44, -621.67, 3049.23), 0.0001298282677479708),
        ((-10000.56, 50000.28, 70000.42), 3.947027197886404e-06),
        ((10000.72, -50000.58, 70000.41), 3.947005115165519e-06),
        ((10000.42, 50000.14, -70000.12), -4.84069027221218e-06)
    ]
])
def test_valores_decimais_negativos(entradas, esperado):
    obtido = calcula_gaussiana(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de x={entradas[0]}, mi={entradas[1]} e sigma={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."
    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'x = {entradas[0]}, mi = {entradas[1]} e sigma = {entradas[2]}')
    for entradas, esperado in [
        ((0, -621, 3049), 0.0001281577162925035),
        ((-10000.32, 0, -70000.23), -5.6412944431564054e-06),
        ((0, 0, 21232), 1.8789670327874564e-05)
    ]
])
def test_valores_com_zeros(entradas, esperado):
    obtido = calcula_gaussiana(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de x={entradas[0]}, mi={entradas[1]} e sigma={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."
    assert obtido == pytest.approx(esperado), mensagem
