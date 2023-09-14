import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import monta_dicionario
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'monta_dicionario')


def test_listas_vazias():
    chaves, valores, dicionario = [], [], {}
    resultado = monta_dicionario(chaves, valores)
    assert resultado == dicionario, f'Algo deu errado na hora de montar o dicionário com {chaves} e {valores}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_listas_de_integers():
    chaves, valores, dicionario = [1,2,3], [4,3,4], {1: 4, 2: 3, 3: 4}
    resultado = monta_dicionario(chaves, valores)
    assert resultado == dicionario, f'Algo deu errado na hora de montar o dicionário com {chaves} e {valores}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_listas_de_strings():
    chaves, valores, dicionario = ['jake', 'la', 'motta'], ['sugar', 'ray', 'robinson'], {'jake': 'sugar', 'la': 'ray', 'motta': 'robinson'}
    resultado = monta_dicionario(chaves, valores)
    assert resultado == dicionario, f'Algo deu errado na hora de montar o dicionário com {chaves} e {valores}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_listas_de_booleanos():
    chaves, valores, dicionario = [True, False], [False, True], {True: False, False: True}
    resultado = monta_dicionario(chaves, valores)
    assert resultado == dicionario, f'Algo deu errado na hora de montar o dicionário com {chaves} e {valores}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_listas_de_strings_e_integers():
    chaves, valores, dicionario = ['batman', 'robin'], [1, 2], {'batman': 1, 'robin': 2}
    resultado = monta_dicionario(chaves, valores)
    assert resultado == dicionario, f'Algo deu errado na hora de montar o dicionário com {chaves} e {valores}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_listas_de_strings_e_caracteres_especiais():
    chaves, valores, dicionario = ['nolan', 'tdk', 'tenet', 'interstellar'], ['!!!!', '!!!!!', '!!!', '!!!!!'], {'nolan': '!!!!', 'tdk': '!!!!!', 'tenet': '!!!', 'interstellar': '!!!!!'}
    resultado = monta_dicionario(chaves, valores)
    assert resultado == dicionario, f'Algo deu errado na hora de montar o dicionário com {chaves} e {valores}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'
