import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import lista_caracteres
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'lista_caracteres')


def test_string_do_exemplo():
    string, lista = 'abacate', ['a', 'b', 'c', 't', 'e']
    resultado = lista_caracteres(string)
    assert resultado == lista, f'Algo deu errado na hora de listar as letras de {string}.\nEra esperado {lista}, mas foi obtido {resultado}.'


def test_string_vazia():
    string, lista = '', []
    resultado = lista_caracteres(string)
    assert resultado == lista, f'Algo deu errado na hora de listar as letras de {string}.\nEra esperado {lista}, mas foi obtido {resultado}.'


def test_string_de_muitas_letras_diferentes():
    string, lista = 'arkhamknight', ['a', 'r', 'k', 'h', 'm', 'n', 'i', 'g', 't']
    resultado = lista_caracteres(string)
    assert resultado == lista, f'Algo deu errado na hora de listar as letras de {string}.\nEra esperado {lista}, mas foi obtido {resultado}.'


def test_string_de_muitas_letras_iguais():
    string, lista = 'robotrock', ['r', 'o', 'b', 't', 'c', 'k']
    resultado = lista_caracteres(string)
    assert resultado == lista, f'Algo deu errado na hora de listar as letras de {string}.\nEra esperado {lista}, mas foi obtido {resultado}.'


def test_string_de_algarismos():
    string, lista = '2049', ['2', '0', '4', '9']
    resultado = lista_caracteres(string)
    assert resultado == lista, f'Algo deu errado na hora de listar as letras de {string}.\nEra esperado {lista}, mas foi obtido {resultado}.'


def test_string_de_caracteres_especiais():
    string, lista = '@*@', ['@', '*']
    resultado = lista_caracteres(string)
    assert resultado == lista, f'Algo deu errado na hora de listar as letras de {string}.\nEra esperado {lista}, mas foi obtido {resultado}.'
