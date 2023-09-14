import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_area_do_triangulo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_area_do_triangulo')


def test_area_triangulo_tipo_de_retorno_e_float():
    base = 1
    altura = 2
    obtido = calcula_area_do_triangulo(base, altura)
    assert type(obtido) == float, f'Algo deu errado o retorno da função não é um valor float, é {type(obtido)}, confirme que esta retornando um valor numérico com casas decimais.'


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'Base = {entradas[0]} e  altura= {entradas[1]}')
    for entradas, esperado in [
        ((2, 2), 2),
        ((3, 5), 7.5),
        ((5, 7), 17.5),
        ((9, 10), 45),
        ((10, 500), 2500),
    ]
])
def test_area_triangulo_com_entrada_somente_de_valores_inteiros(entradas, esperado):
    base = entradas[0]
    altura = entradas[1]
    esperado = esperado
    obtido = calcula_area_do_triangulo(base, altura)
    assert obtido == esperado, f'Algo deu de errado, era esperado {esperado}, mas foi obtido {obtido}.'


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'Base = {entradas[0]} e  altura= {entradas[1]}')
    for entradas, esperado in [
        ((2.5, 2), 2.5),
        ((3, 5.8), 8.7),
        ((5, 3.6), 9),
        ((9.5, 4), 19),
        ((14.6, 2.6), 18.98),
    ]
])
def test_area_triangulo_com_entrada_de_alguns_valores_com_casas_decimais(entradas, esperado):
    base = entradas[0]
    altura = entradas[1]
    esperado = esperado
    obtido = calcula_area_do_triangulo(base, altura)
    assert obtido == esperado, f'Algo deu de errado, era esperado {esperado}, mas foi obtido {obtido}.'
