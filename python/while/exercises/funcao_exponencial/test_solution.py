import pytest
from pytest import approx
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_euler
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_euler')


@pytest.mark.timeout(5)
def test_do_exemplo():
    x, n = 5, 6
    euler_calculado = calcula_euler(x, n)
    esperado = 91.41666666666667
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'


@pytest.mark.timeout(5)
def test_somente_elemento_inicial():
    x, n = 1, 1
    euler_calculado = calcula_euler(x, n)
    esperado = 1
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'


@pytest.mark.timeout(5)
def test_com_n_nulo():
    x, n = 10, 0
    euler_calculado = calcula_euler(x, n)
    esperado = 0
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'


@pytest.mark.timeout(5)
def test_com_x_nulo():
    x, n = 0, 10
    euler_calculado = calcula_euler(x, n)
    esperado = 1
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'


@pytest.mark.timeout(5)
def test_com_n_grande():
    x, n = 5, 10
    euler_calculado = calcula_euler(x, n)
    esperado = 143.6894565696649
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'


@pytest.mark.timeout(5)
def test_com_x_grande():
    x, n = 10, 5
    euler_calculado = calcula_euler(x, n)
    esperado = 644.3333333333334
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'


@pytest.mark.timeout(5)
def test_com_x_n_grandes():
    x, n = 10, 10
    euler_calculado = calcula_euler(x, n)
    esperado = 10086.573192239859
    assert euler_calculado == approx(esperado), f'Algo deu errado ao calcular euler para x={x} e n={n}.\nEra esperado {esperado} mas foi obtido {euler_calculado}.'
