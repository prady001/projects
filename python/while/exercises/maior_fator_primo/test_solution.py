import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import maior_fator_primo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'maior_fator_primo')


@pytest.mark.timeout(10)
@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado,
                 id=f'{entrada}')
    for entrada, esperado in [
        (5, 5),
        (54, 3),
        (312874621893, 7139833),
    ]
])
def test_fatores_primos(entrada, esperado):
    obtido = maior_fator_primo(entrada)
    mensagem = f"Algo deu errado ao testar o valor{entrada}. O esperado era {esperado}, mas foi obtido {obtido}."

    assert obtido == esperado, mensagem
