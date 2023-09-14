import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_pi
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_pi')


@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado,
                 id=f'{entrada}')
    for entrada, esperado in [
        (1, 2.449489742783178),
        (2, 2.7386127875258306),
        (3, 2.857738033247041),
        (4, 2.92261298612503),
        (10, 3.04936163598207),
        (100, 3.132076531809106),
        (1000, 3.140638056205993),
        (10000, 3.1414971639472147)
    ]
])
@pytest.mark.timeout(5)
def test_valor_estimado_pi(entrada, esperado):
    obtido = calcula_pi(entrada)
    mensagem = f'Algo deu errado ao testar o valor {entrada}. O esperado era {esperado}, mas foi obtido {obtido}.'
    if abs(obtido-esperado**2) < 0.01:
        mensagem += ' Uma dica: verifique a raiz quadrada.'

    assert obtido == pytest.approx(esperado), mensagem
