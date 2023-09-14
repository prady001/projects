import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import alunos_impares
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'alunos_impares')


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'{entradas}')
    for entradas, esperado in [
        (['aluno1'], []),
        (['aluno1', 'aluno2', 'aluno3', 'aluno4', 'aluno5'], ['aluno2', 'aluno4']),
        ([], []),
    ]
])
def test_alunos(entradas, esperado):
    obtido = alunos_impares(entradas)
    mensagem = f'Algo deu errado ao testar a lista {entradas}. O esperado era {esperado}, mas foi obtido {obtido}.'

    assert obtido == esperado, mensagem
