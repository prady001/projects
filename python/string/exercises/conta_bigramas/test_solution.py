import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import conta_bigramas
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'conta_bigramas')


def test_string_vazia():
    string, dicionario_bigramas = '', {}
    resultado = conta_bigramas(string)
    assert resultado == dicionario_bigramas, f'Algo deu errado na hora de contar os bigramas de {string}.\nEra esperado {dicionario_bigramas}, mas foi obtido {resultado}.'


def test_string_do_exemplo():
    string, dicionario_bigramas = 'banana nanica', {'ba': 1, 'an': 3, 'na': 3, 'a ': 1, ' n': 1, 'ni': 1, 'ic': 1, 'ca': 1}
    resultado = conta_bigramas(string)
    assert resultado == dicionario_bigramas, f'Algo deu errado na hora de contar os bigramas de {string}.\nEra esperado {dicionario_bigramas}, mas foi obtido {resultado}.'


def test_string_de_algarismos():
    string, dicionario_bigramas = '2049', {'20': 1, '04': 1, '49': 1}
    resultado = conta_bigramas(string)
    assert resultado == dicionario_bigramas, f'Algo deu errado na hora de contar os bigramas de {string}.\nEra esperado {dicionario_bigramas}, mas foi obtido {resultado}.'


def test_string_de_caracteres_especiais():
    string, dicionario_bigramas = '*:)*', {'*:': 1, ':)': 1, ')*': 1}
    resultado = conta_bigramas(string)
    assert resultado == dicionario_bigramas, f'Algo deu errado na hora de contar os bigramas de {string}.\nEra esperado {dicionario_bigramas}, mas foi obtido {resultado}.'


def test_string_de_repetidos():
    string, dicionario_bigramas = 'pula-pula', {'pu': 2, 'ul': 2, 'la': 2, 'a-': 1, '-p': 1}
    resultado = conta_bigramas(string)
    assert resultado == dicionario_bigramas, f'Algo deu errado na hora de contar os bigramas de {string}.\nEra esperado {dicionario_bigramas}, mas foi obtido {resultado}.'
