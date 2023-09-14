import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import maior_primo_menor_que
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'maior_primo_menor_que')


@pytest.mark.timeout(5)
def test_numero_negativo():
    n, primo = -10, -1
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_numero_0():
    n, primo = 0, -1
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_numero_1():
    n, primo = 1, -1
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_numero_primo():
    n, primo = 2, 2
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_outro_numero_primo():
    n, primo = 3, 3
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_numero_nao_primo():
    n, primo = 10, 7
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_numero_nao_primo_grande():
    n, primo = 1000, 997
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'


@pytest.mark.timeout(5)
def test_numero_nao_primo_muito_grande():
    n, primo = 6900, 6899
    resultado = maior_primo_menor_que(n)
    assert resultado == primo, f'Algo deu errado na hora de descobrir o maior primo menor que {n}.\nEra esperado {primo}, mas foi obtido {resultado}.'
