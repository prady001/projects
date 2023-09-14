import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import reflexao_total_interna
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'reflexao_total_interna')


gabarito = [([1, 1, 90], False), ([1, 1, 180], False), ([1, 1, 270], False), ([1, 1, 360], False), ([0.5, 1, 0], False),
([0.5, 1, 60], True), ([0.5, 1, 120], True), ([0.5, 1, 250], False), ([1, 0.5, 0], False), ([1, 0.5, 275], False),
([1.5, 1.74, 90], True), ([1.5, 1.74, 120], True)]


@pytest.mark.parametrize(
    'entradas, resposta', [
        pytest.param(
            entradas,
            resposta,
            id = f'n1 = {entradas[0]}, n2 = {entradas[1]}, teta2 = {entradas[2]}, resposta: {resposta}'
        )
        for entradas, resposta in gabarito
    ])
def test_verifica_reflexão(entradas, resposta):
    resultado = reflexao_total_interna(entradas[0], entradas[1], entradas[2])
    assert resultado == resposta, f'Não funcionou para {entradas}.\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'
