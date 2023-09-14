import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import maximo_divisor_comum
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'maximo_divisor_comum')


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'{entradas}')
    for entradas, esperado in [
        ((1, 2), 1),
        ((32, 79), 1),
        ((189, 54), 27),
        ((5538, 1105), 13),
        ((1425, 24225), 1425)
    ]
])
@pytest.mark.timeout(5)
def test_máximo_divisor_comum(entradas, esperado):
    obtido = maximo_divisor_comum(entradas[0], entradas[1])
    mensagem = f'Algo deu errado ao testar o valores {entradas[0]} e {entradas[1]}. O esperado era {esperado}, mas foi obtido {obtido}.'
    assert obtido == esperado, mensagem
