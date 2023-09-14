import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import pos_arroba
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'pos_arroba')


def test_string_do_exemplo():
    string, posicao = 'andre1234@insper.edu.br', 9
    resultado = pos_arroba(string)
    assert resultado == posicao, f'Algo deu errado na hora de verificar a posição do arroba em {string}.\nEra esperado {posicao}, mas foi obtido {resultado}.'


def test_string_generica():
    string, posicao = 'usuario@insper.edu.br', 7
    resultado = pos_arroba(string)
    assert resultado == posicao, f'Algo deu errado na hora de verificar a posição do arroba em {string}.\nEra esperado {posicao}, mas foi obtido {resultado}.'
