import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import conta_letras
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'conta_letras')


def test_string_vazia():
    palavra, dicionario = '', {}
    resultado = conta_letras(palavra)
    assert resultado == dicionario, f'Algo deu errado na hora de contar as letras de {palavra}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_string_de_muitas_letras_diferentes():
    palavra, dicionario = 'arkham knight', {'a': 2, 'r': 1, 'k': 2, 'h': 2, 'm': 1, ' ': 1, 'n': 1, 'i': 1, 'g': 1, 't': 1}
    resultado = conta_letras(palavra)
    assert resultado == dicionario, f'Algo deu errado na hora de contar as letras de {palavra}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_string_de_muitas_letras_iguais():
    palavra, dicionario = 'peter parker', {'p': 2, 'e': 3, 't': 1, 'r': 3, ' ': 1, 'a': 1, 'k': 1}
    resultado = conta_letras(palavra)
    assert resultado == dicionario, f'Algo deu errado na hora de contar as letras de {palavra}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_string_de_algarismos():
    palavra, dicionario = '2049', {'2': 1, '0': 1, '4': 1, '9': 1}
    resultado = conta_letras(palavra)
    assert resultado == dicionario, f'Algo deu errado na hora de contar as letras de {palavra}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'


def test_string_de_caracteres_especiais():
    palavra, dicionario = '@*@', {'@': 2, '*': 1}
    resultado = conta_letras(palavra)
    assert resultado == dicionario, f'Algo deu errado na hora de contar as letras de {palavra}.\nEra esperado {dicionario}, mas foi obtido {resultado}.'
