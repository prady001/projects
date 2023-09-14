import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import verifica_progressao
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'verifica_progressao')


gabarito = [([1, 1, 1, 1, 1, 1, 1], 'AG'), ([100, 100, 100, 100, 100, 100, 100], 'AG'), ([9, 9, 9, 9, 9], 'AG'),
([0, 0, 0, 0, 0, 0, 0], 'PA'), ([0, 1, 2, 3, 4, 5, 6], 'PA'), ([0, 2, 4, 6, 8, 10, 12], 'PA'),
([13, 26, 39, 52, 65, 78], 'PA'), ([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], 'PA'), ([0, -1, -2, -3, -4, -5, -6], 'PA'),
([0, -2, -4, -6, -8, -10, -12], 'PA'), ([26, 13, 0, -13, -26, -39, -52, -65, -78], 'PA'),
([4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0, -0.5, -1, -1.5, -2, -2.5, -3, -3.5, -4], 'PA'), ([1, 2, 4, 8, 16, 32], 'PG'),
([3, 9, 27, 81], 'PG'), ([32, 16, 8, 4, 2, 1, 0.5, 0.25], 'PG'), ([1, 5, 25, 125, 625], 'PG'), ([1, -1, 1, -1, 1, -1], 'PG'),
([3, -9, 27, -81], 'PG'), ([32, -16, 8, -4, 2, -1, 0.5, -0.25], 'PG'), ([1, -5, 25, -125, 625], 'PG')]


@pytest.mark.timeout(5)
@pytest.mark.parametrize(
    'lista, resposta', [
        pytest.param(
            lista,
            resposta,
            id = f'lista: {lista}; resposta: {resposta}'
        )
        for lista, resposta in gabarito
    ])
def test_verifica_PA_PG(lista, resposta):
    resultado = verifica_progressao(lista)
    assert resultado == resposta, f'Não funcionou para {lista}.\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'
