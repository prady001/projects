import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import conta_a
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'conta_a')


def test_string_com_poucos_a():
    entrada = 'aldeia'
    obtido = conta_a(entrada)
    esperado = 2
    assert obtido == esperado,  f'Algo deu errado na contagem da string {entrada}. \nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_string_com_muitos_a():
    entrada = 'banana amarela'
    obtido = conta_a(entrada)
    esperado = 6
    assert obtido == esperado,  f'Algo deu errado na contagem da string {entrada}. \nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_string_sem_a():
    entrada = 'esquecimento'
    obtido = conta_a(entrada)
    esperado = 0
    assert obtido == esperado,  f'Algo deu errado na contagem da string {entrada}, que não possui a letra "a". \nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_string_vazia():
    string = ''
    obtido = conta_a(string)
    esperado = 0
    assert obtido == esperado,  f'Algo deu errado na contagem com strings vazias. \nEra esperado {esperado}, mas foi obtido {obtido}.'
