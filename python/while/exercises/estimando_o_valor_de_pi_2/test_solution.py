import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import PiWallis
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'PiWallis')


@pytest.mark.parametrize('entrada, esperado, anterior, proximo', [
    pytest.param(entrada, esperado, anterior, proximo,
                 id=f'{entrada}')
    for entrada, esperado, anterior, proximo in [
        (1, 4.0, 2, 2.6666666666666665),
        (2, 2.6666666666666665, 4.0, 3.5555555555555554),
        (3, 3.5555555555555554, 2.6666666666666665, 2.8444444444444446),
        (4, 2.8444444444444446, 3.5555555555555554, 3.4133333333333336),
        (10, 3.0021759545569062, 3.302393550012597, 3.2751010413348065),
        (100, 3.126078900215409, 3.157339689217563, 3.1570301764551654),
        (1000, 3.140023818600586, 3.143163842419187, 3.1431607055322552),
        (10000, 3.1414355935898644, 3.1417497371492233, 3.1417497057380084)
    ]
])
@pytest.mark.timeout(5)
def test_valor_estimado_pi(entrada, esperado, anterior, proximo):
    obtido = PiWallis(entrada)
    mensagem = f'Algo deu errado ao testar o valor {entrada}. O esperado era {esperado}, mas foi obtido {obtido}.'
    if obtido == pytest.approx(anterior, abs=1e-12):
        mensagem += ' Será que você não está calculando com um elemento a menos da série?'
    if obtido == pytest.approx(proximo, abs=1e-12):
        mensagem += ' Será que você não está calculando com um elemento a mais da série?'
    if obtido == pytest.approx(esperado/2):
        mensagem += ' Note que o resultado da soma é pi/2, mas queremos o valor de pi.'
    assert obtido == pytest.approx(esperado), mensagem
