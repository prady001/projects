import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import volume_da_pizza
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'volume_da_pizza')


@pytest.mark.parametrize(
    'z, a, esperado',
    [
        pytest.param(z, a, esperado, id=f'z={z}, a={a}')
        for z, a, esperado in [
            (0, 10, 0),
            (10, 0, 0),
            (1, 1, 3.141592653589793),
            (10, 2, 628.3185307179587),
            (10.5, 2.5, 865.9014751456867),
            (0.3, 10.3, 2.9122563898777387),
            (10.6, 0.4, 141.19574022293966),
            (1.5, 1.5, 10.602875205865551),
        ]
    ]
)
def test_calculando_volume_da_pizza(z, a, esperado):
    obtido = volume_da_pizza(z, a)
    assert obtido == pytest.approx(esperado), f'Algo deu errado ao calcular o volume da pizza para o raio z = {z} e altura a = {a}.\nEra esperado {esperado}, mas obtido foi {obtido}.\nVerifique se está passando os argumentos na orgem correta.'
