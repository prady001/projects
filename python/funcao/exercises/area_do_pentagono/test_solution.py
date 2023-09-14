import pytest
from pytest import approx
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_area_do_pentagono
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_area_do_pentagono')


def test_area_pentagono_tipo_de_retorno_e_float():
    lado = 1
    obtido = calcula_area_do_pentagono(lado)
    assert type(obtido) == float, f'Algo deu errado, o retorno da função não é um valor float, é {type(obtido)}, confirme que esta retornando um valor numérico com casas decimais.'


@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado,
                 id=f'Lado = {entrada}')
    for entrada, esperado in [
        (2, 6.881909),
        (3, 15.484296),
        (5, 43.011935),
        (9, 139.358669),
        (10, 172.047740),
    ]
])
def test_area_pentagono(entrada, esperado):
    obtido = calcula_area_do_pentagono(entrada)
    assert obtido == approx(esperado) , f'Algo deu de errado, era esperado {esperado}, mas foi obtido {obtido}.'
