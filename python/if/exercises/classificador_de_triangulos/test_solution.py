import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import classifica_triangulo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'classifica_triangulo')


gabarito = [
    ('equilátero', (7, 7, 7)),
    ('equilátero', (1.2, 1.2, 1.2)),
    ('isósceles', (9, 21.8, 21.8)),
    ('isósceles', (2, 31, 2)),
    ('isósceles', (5, 5, 8)),
    ('escaleno', (38, 1, 29)),
    ('escaleno', (15, 5, 2.5)),
]


@pytest.mark.parametrize(
    'classificacao, lados',
    [
        pytest.param(classificacao, lados, id=str(lados))
        for classificacao, lados in gabarito
    ]

)
def test_classifica_triangulo(classificacao, lados):
    obtido = classifica_triangulo(*lados)
    msg = f'Algo deu errado com o triângulo {lados}. Era esperado {classificacao} mas foi obtido {obtido}.'
    assert classificacao == obtido, msg
