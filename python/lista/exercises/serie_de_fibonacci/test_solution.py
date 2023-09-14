import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_fibonacci
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_fibonacci')


@pytest.mark.timeout(5)
def test_um_termo():
    num_test = 1
    resposta = [1]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_dois_termos():
    num_test = 2
    resposta = [1, 1]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_tres_termos():
    num_test = 3
    resposta = [1, 1, 2]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_quatro_termos():
    num_test = 4
    resposta = [1, 1, 2, 3]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_cinco_termos():
    num_test = 5
    resposta = [1, 1, 2, 3, 5]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_seis_termos():
    num_test = 6
    resposta = [1, 1, 2, 3, 5, 8]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_sete_termos():
    num_test = 7
    resposta = [1, 1, 2, 3, 5, 8, 13]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_oito_termos():
    num_test = 8
    resposta = [1, 1, 2, 3, 5, 8, 13, 21]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_nove_termos():
    num_test = 9
    resposta = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_dez_termos():
    num_test = 10
    resposta = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.timeout(5)
def test_vinte_termos():
    num_test = 20
    resposta = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    resultado = calcula_fibonacci(num_test)
    assert resultado == resposta, f'Não funcionou para o número {num_test}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'
