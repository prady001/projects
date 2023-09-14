import pytest
from pytest_devlife import util

try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import fatorial
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'fatorial')


gabarito = [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720), (7, 5040), (8, 40320), (9, 362880), (10, 3628800), (11, 39916800), (12, 479001600), (13, 6227020800), (14, 87178291200), (15, 1307674368000), (16, 20922789888000), (17, 355687428096000), (18, 6402373705728000), (19, 121645100408832000), (20, 2432902008176640000)]


@pytest.mark.parametrize(
    'n, esperado',
    [
        pytest.param(n, esperado, id=f'{n}!')
        for n, esperado in gabarito
    ]
)
def test_fatorial(n, esperado):
    obtido = fatorial(n)
    assert obtido == esperado, f'Algo deu errado com a entrada {n}. Era esperado {esperado} mas foi obtido {obtido}.'
