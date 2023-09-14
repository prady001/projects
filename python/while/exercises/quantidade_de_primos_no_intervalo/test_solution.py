import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import primos_entre
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'primos_entre')



@pytest.mark.timeout(5)
@pytest.mark.parametrize('a,b', [
    pytest.param(a, b, id=f'a = {a}, b = {b}')
    for a, b in [
        (14, 16),
        (24, 28),
        (90, 96),
    ]
])
def test_nenhum_número_primo_no_intervalo(a, b):
    obtido = primos_entre(a, b)
    assert obtido == 0, f'Algo deu errado para o intervalo de {a} até {b}. Era esperado "0", porém foi obtido "{obtido}".'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('a,b', [
    pytest.param(a, b, id=f'a = {a}, b = {b}')
    for a, b in [
        (4, 6),
        (44, 47),
        (53, 58),
        (90, 100),
    ]
])
def test_um_número_primo_no_intervalo(a, b):
    obtido = primos_entre(a, b)
    assert obtido == 1, f'Algo deu errado para o intervalo de {a} até {b}. Era esperado "1", porém foi obtido "{obtido}".'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('a,b', [
    pytest.param(a, b, id=f'a = {a}, b = {b}')
    for a, b in [
        (2, 3),
        (84, 100),
    ]
])
def test_dois_números_primos_no_intervalo(a, b):
    obtido = primos_entre(a, b)
    assert obtido == 2, f'Algo deu errado para o intervalo de {a} até {b}. Era esperado "2", porém foi obtido "{obtido}".'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('a, b, esperado', [
    pytest.param(a, b, esperado, id=f'a = {a}, b = {b}')
    for a, b, esperado in [
        (450, 500, 8),
        (10, 100, 21),
        (2, 100, 25),
    ]
])
def test_alguns_números_primos_no_intervalo(a, b, esperado):
    obtido = primos_entre(a, b)
    assert obtido == esperado, f'Algo deu errado para o intervalo de {a} até {b}. Era esperado "{esperado}", porém foi obtido "{obtido}".'
