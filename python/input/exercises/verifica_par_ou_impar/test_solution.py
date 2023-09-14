import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import verifica_par_ou_impar
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'verifica_par_ou_impar')


lista_pares = [2, 10, 14, 58, 106, 2700, 473628958, 13500006, 8984538252, 1200000000000]
@pytest.mark.parametrize(
    'par',
    [
        pytest.param(i, id=f'par={i}') for i in lista_pares
    ]
)
def test_numeros_pares(par):
    obtido = verifica_par_ou_impar(par)
    assert obtido == 1, f'Algo deu errado na classificação de numeros pares.\nPara a entrada {par}, era esperado 1, mas foi obtido {obtido}.'


lista_impares = [1, 3, 7, 19, 57, 1457, 22222227, 912469, 7452846845, 1800000000003]
@pytest.mark.parametrize(
    'impar',
    [
        pytest.param(i, id=f'impar={i}') for i in lista_impares
    ]
)
def test_numeros_impares(impar):
    obtido = verifica_par_ou_impar(impar)
    assert obtido == -1, f'Algo deu errado na classificação de numeros impares.\nPara a entrada {impar}, era esperado 1, mas foi obtido {obtido}.'


lista_pares_neg = [-2, -10, -14, -58, -106, -2700, -473628958, -13500006, -8984538252, -1200000000000]
@pytest.mark.parametrize(
    'par',
    [
        pytest.param(i, id=f'par={i}') for i in lista_pares_neg
    ]
)
def test_pares_negativos(par):
    obtido = verifica_par_ou_impar(par)
    assert obtido == 1, f'Algo deu errado na classificação de numeros pares negativos.\nPara a entrada {par}, era esperado 1, mas foi obtido {obtido}.'


lista_impares_neg = [-1, -3, -7, -19, -57, -1457, -22222227, -912469, -7452846845, -1800000000003]
@pytest.mark.parametrize(
    'impar',
    [
        pytest.param(i, id=f'impar={i}') for i in lista_impares_neg
    ]
)
def test_impares_negativos(impar):
    obtido = verifica_par_ou_impar(impar)
    assert obtido == -1, f'Algo deu errado na classificação de numeros impares negativos.\nPara a entrada {impar}, era esperado -1, mas foi obtido {obtido}.'


def test_entrada_zero():
    obtido = verifica_par_ou_impar(0)
    assert obtido == 1, f'Algo deu errado na classificação do numero 0 (zero).\nEra esperado 1, mas foi obtido {obtido}.'
