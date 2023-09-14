import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import aproxima_raiz
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'aproxima_raiz')

@pytest.mark.timeout(5)
def test_saida_e_numero_inteiro():
    numero = 4
    obtido = aproxima_raiz(numero)
    assert type(obtido) == int, 'Algo deu errado, o retorno da função não é um número inteiro, confirme que está retornando um integer (type = int).'


@pytest.mark.parametrize(
    'numero, esperado',
    [
        pytest.param(numero, esperado, id=f'numero={numero}, esperado={esperado}') for numero, esperado in [(3,2),(4,2),(17,4),(36,6),(55,7),(121,11),(178,13),(520,23),(625,25),(3049,55)]
    ]
)
@pytest.mark.timeout(5)
def test_raiz_quadrada_aproximada_de(numero, esperado):
    obtido = aproxima_raiz(numero)
    assert obtido == esperado, f'Algo deu errado, era esperado {esperado}, mas foi obtido {obtido}, confirme que está comparando i e i-1 e que o quadrado de i é maior ou igual ao número {numero}.'
