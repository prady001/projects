import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import primeiras_ocorrencias
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'primeiras_ocorrencias')


def test_uma_palavra():
    string = 'abracadabra'
    esperado = {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
    obtido = primeiras_ocorrencias(string)
    assert obtido == esperado, f'Algo deu errado para strings com uma unica palavra.\nPara a entrada "{string}", era esperado {esperado}, mas foi obtido {obtido}.'


def test_mais_de_uma_palavra():
    string = 'a menina que roubava livros'
    esperado = {'a': 0, ' ': 1, 'm': 2, 'e': 3, 'n': 4, 'i': 5, 'q': 9, 'u': 10, 'r': 13, 'o': 14, 'b': 16, 'v': 18, 'l': 21, 's': 26}
    obtido = primeiras_ocorrencias(string)
    assert obtido == esperado, f'Algo deu errado para strings com mais de uma palavra.\nPara a entrada "{string}", era esperado {esperado} mas foi obtido {obtido}.'


def test_string_vazia():
    string = ''
    esperado = {}
    obtido = primeiras_ocorrencias(string)
    assert obtido == esperado, f'Algo deu errado para strings vazias.\nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_string_com_algarismos():
    string = '101 dalmatas'
    esperado = {'1': 0, '0': 1, ' ': 3, 'd': 4, 'a': 5, 'l': 6, 'm': 7, 't': 9, 's': 11}
    obtido = primeiras_ocorrencias(string)
    assert obtido == esperado, f'Algo deu errado para strings com numeros.\nPara a entrada "{string}", era esperado {esperado} mas foi obtido {obtido}.'


def test_caracteres_especiais():
    string = '@!?*!!@'
    esperado = {'@': 0, '!': 1, '?': 2, '*': 3}
    obtido = primeiras_ocorrencias(string)
    assert obtido == esperado, f'Algo deu errado para strings com caracteres especiais.\nPara a entrada "{string}", era esperado {esperado}, mas foi obtido {obtido}.'
