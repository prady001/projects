import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import x_maior_que_y
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'x_maior_que_y')


x_maior  = [i for i in range(1, 10)]
x_menor  = [i - 1 for i in range(1, 10)]
x_igual  = [i for i in range(1, 10)]
x_aleatorio = [5, 12, 91, 1, 55, 12, 9]

y_maior  = [i - 1 for i in range(1, 10)]
y_menor  = [i for i in range(1, 10)]
y_igual  = [i for i in range(1, 10)]
y_aleatorio = [60, 6, 23, 1, 5, 2, 77]

respostas_aleatorio = [0, 1, 1, 0, 1, 1, 0]


@pytest.mark.parametrize("x,y,expected",
    [
        pytest.param(x_maior[i], y_maior[i], 1, id = f"x={x_maior[i]}, y={y_maior[i]}") for i in range(len(x_maior))
    ]
)
def test_x_e_maior_que_y(x, y, expected):
    reposta = x_maior_que_y(x, y)
    msg = f"Parece que algo deu errado. O que acontece no caso em que x e y são iguais?"
    assert reposta == expected, msg


@pytest.mark.parametrize("x,y,expected",
    [
        pytest.param(x_menor[i], y_menor[i], 0, id = f"x={x_menor[i]}, y={y_menor[i]}") for i in range(len(x_maior))
    ]
)
def test_x_e_menor_que_y(x, y, expected):
    reposta = x_maior_que_y(x, y)
    msg = f"Parece que algo deu errado. O esperado era {expected}, mas o recebido foi {reposta}."
    assert reposta == expected, msg


@pytest.mark.parametrize("x,y,expected",
    [
        pytest.param(x_igual[i], y_igual[i], 0, id = f"x={x_igual[i]}, y={y_igual[i]}") for i in range(len(x_maior))
    ]
)
def test_x_e_igual_que_y(x, y, expected):
    reposta = x_maior_que_y(x, y)
    msg = f"Parece que algo deu errado. O que acontece no caso em que x e y são iguais?"
    assert reposta == expected, msg


@pytest.mark.parametrize("x,y,expected",
    [
        pytest.param(x_aleatorio[i], y_aleatorio[i], respostas_aleatorio[i], id = f"x={x_aleatorio[i]}, y={y_aleatorio[i]}") for i in range(len(x_aleatorio))
    ]
)
def test_x_e_maior_que_y_arbitrario(x, y, expected):
    reposta = x_maior_que_y(x, y)
    msg = f"Parece que algo deu errado. O esperado era {expected}, mas o recebido foi {reposta}."
    if x == y:
        msg = f"Parece que algo deu errado. O que acontece no caso em que x e y são iguais?"
    assert reposta == expected, msg
