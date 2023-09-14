import pytest
import pprint
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import encontra_maximo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'encontra_maximo')


@pytest.mark.timeout(5)
def test_matriz_do_exemplo():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    norma_infinito = 9
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_matriz_nula():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    norma_infinito = 0
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha1_coluna1():
    matriz = [[110, 12, 13], [21, 22, 23], [31, 32, 33]]
    norma_infinito = 110
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha1_coluna2():
    matriz = [[11, 120, 13], [21, 22, 23], [31, 32, 33]]
    norma_infinito = 120
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha1_coluna3():
    matriz = [[11, 12, 130], [21, 22, 23], [31, 32, 33]]
    norma_infinito = 130
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha2_coluna1():
    matriz = [[11, 12, 13], [210, 22, 23], [31, 32, 33]]
    norma_infinito = 210
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha2_coluna2():
    matriz = [[11, 12, 13], [21, 220, 23], [31, 32, 33]]
    norma_infinito = 220
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha2_coluna3():
    matriz = [[11, 12, 13], [21, 22, 230], [31, 32, 33]]
    norma_infinito = 230
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha3_coluna1():
    matriz = [[11, 12, 13], [21, 22, 23], [310, 32, 33]]
    norma_infinito = 310
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha3_coluna2():
    matriz = [[11, 12, 13], [21, 22, 23], [31, 320, 33]]
    norma_infinito = 320
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_norma_infinito_na_linha3_coluna3():
    matriz = [[11, 12, 13], [21, 22, 23], [31, 32, 330]]
    norma_infinito = 330
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_elemento_negativo_como_norma_infinita():
    matriz = [[1, 2, 3], [-10, 5, 6], [7, 8, 9]]
    norma_infinito = 10
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_tem_elemento_negativo_mas_nao_eh_norma_infinita():
    matriz = [[1, 2, 3], [-10, 5, 6], [20, 8, 9]]
    norma_infinito = 20
    resultado = encontra_maximo(matriz)
    assert resultado == norma_infinito, f'Algo deu errado na hora de obter a norma infinito da matriz {pprint.pformat(matriz)}.\nEra esperado {norma_infinito}, mas foi obtido {resultado}.'
