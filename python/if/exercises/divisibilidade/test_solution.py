import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import divisivel
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'divisivel')


@pytest.mark.parametrize('numero', [1, 5, 7, 13])
def test_numeros_nao_divisiveis_nem_por_2_nem_por_3(numero):
    assert divisivel(numero) == numero, f'O número inserido não é divisível nem por 2 nem por 3, ele é {numero}'


@pytest.mark.parametrize('numero', [2, 4, 8, 200])
def test_numeros_divisiveis_somente_por_2(numero):
    assert divisivel(numero) == 'Ins', f'O número {numero} é divisível somente por 2'


@pytest.mark.parametrize('numero', [3, 9, 15, 21, 33, 39])
def test_numeros_divisiveis_somente_por_3(numero):
    assert divisivel(numero) == 'per', f'O número {numero} é divisível somente por 3'


@pytest.mark.parametrize('numero', [6, 12, 36, 150, 330, 660])
def test_numeros_divisiveis_por_2_e_por_3(numero):
    assert divisivel(numero) == 'Insper', f'O número {numero} é divisível por 2 e por 3'
