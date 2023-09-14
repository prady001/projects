import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import raiz_quadrada
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'raiz_quadrada')


@pytest.mark.parametrize(
    'num, raiz',
    [
        pytest.param(i**2, i, id=f'x={i**2}, y={i}') for i in range(0, 101)
    ]
)
@pytest.mark.timeout(5)
def test_raiz_inteira_de_x_resultando_em_y(num, raiz):
    resultado = raiz_quadrada(num)
    assert resultado == raiz, f'Algo deu de errado na raiz quadrada do número {num}.\nEra esperado {raiz}, mas foi obtido {resultado}.'
