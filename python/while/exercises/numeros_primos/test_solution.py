import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import eh_primo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'eh_primo')


lista_200_primeiros_numeros = [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, True]

@pytest.mark.parametrize(
    'n, primo',
    [
        pytest.param(i, primo, id=f'n = {i}') for i, primo in enumerate(lista_200_primeiros_numeros)
    ]
)
@pytest.mark.timeout(0.5)
def test_eh_primo_de_0_a_200(n, primo):
    resultado = eh_primo(n)
    assert resultado == primo, f'Algo deu errado na hora de verificar se {n} é primo.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.parametrize(
    'n',
    [
        pytest.param(i, id=f'n = {i}') for i in range(-10,0)
    ]
)
@pytest.mark.timeout(0.5)
def test_eh_primo_de_números_negativos(n):
    resultado = eh_primo(n)
    assert resultado == False, f'Algo deu errado na hora de verificar se {n} é primo.\nEra esperado {False}, mas foi obtido {resultado}.'
