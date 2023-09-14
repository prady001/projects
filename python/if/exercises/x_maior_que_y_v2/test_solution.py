import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import x_maior_que_y_2
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'x_maior_que_y_2')


@pytest.mark.parametrize('x, y, expected', [
    pytest.param(2*i, i, 1, id=f"x={2*i} e y={i}") for i in range(1, 100, 2)
])
def test_x_maior_que_y(x, y, expected):
    resposta = x_maior_que_y_2(x, y)
    assert resposta == expected, f'Para x={x} e y={y} era esperado receber 1 e o valor obtido foi {resposta}'


@pytest.mark.parametrize('x, y, expected', [
    pytest.param(i, i, 0, id = f"x={i} e y={i}") for i in range(1, 100, 2)
])
def test_x_igual_y(x, y, expected):
    resposta = x_maior_que_y_2(x, y)
    assert resposta == expected, f'Para x={x} e y={y} era esperado receber 0 e o valor obtido foi {resposta}'


@pytest.mark.parametrize('x, y, expected', [
    pytest.param(i, 2*i, -1, id = f"x={i} e y={2*i}") for i in range(1, 100, 2)
])
def test_x_menor_que_y(x, y, expected):
    resposta = x_maior_que_y_2(x, y)
    assert resposta == expected, f'Para x={x} e y={y} era esperado receber -1 e o valor obtido foi {resposta}'
