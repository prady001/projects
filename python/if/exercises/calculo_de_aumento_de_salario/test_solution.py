import pytest
import math
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_aumento
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_aumento')


@pytest.mark.parametrize("salario",
    [
        pytest.param(i, id = f"salario={i}") for i in list(range(1000, 2001, 20)) + list(range(1245, 1255))
    ]
)
def test_calcula_aumento_de_salario_para(salario):
    expected = salario * (0.1 + 0.05 * (salario <= 1250))
    ans = calcula_aumento(salario)

    msg = f"Parece que algo deu errado. O esperado para um salário de R${salario} era R${expected:.2f}, mas recebemos R${ans:.2f}."
    if ans == pytest.approx(salario + expected, rel = 1e-3):
        msg = f"{msg} Note que o enunciado pede que a função devolva o aumento, não o valor total do novo salário."

    assert ans == pytest.approx(expected, rel = 1e-3), msg
