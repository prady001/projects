import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import aniversariantes_de_setembro
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'aniversariantes_de_setembro')


def test_aniversariantes_de_setembro():
    entrada = {
        'Nico Uno': '01/01/1992',
        'Horácio P. Genaro': '03/03/1992',
        'Ukibe Nokome': '05/05/1992',
        'Maurício Melo': '07/09/1992',
        'Abigail Oliveira': '09/09/1992',
    }
    esperado = {'Maurício Melo': '07/09/1992', 'Abigail Oliveira': '09/09/1992'}
    obtido = aniversariantes_de_setembro(entrada)
    msg = f'Algo deu errado com o dicionário {entrada}.\n Era esperado {esperado} mas foi obtido {obtido}'
    assert obtido == esperado, msg


def test_nenhum_aniversariante_em_setembro():
    entrada = {
        'Felipe Correia': '01/01/1993',
        'Horácio P. Genaro': '06/03/1992',
        'Enzo Nakamura': '07/11/1992',
    }
    obtido = aniversariantes_de_setembro(entrada)
    esperado = {}
    msg = f'Algo deu errado com o dicionário {entrada}.\n Era esperado {esperado} mas foi obtido {obtido}'
    assert obtido == esperado, msg


def test_dicionario_vazio():
    obtido = aniversariantes_de_setembro({})
    msg = f'Sua função não funcionou para um dicionário vazio. Era esperado um dicionário vazio, mas foi obtido {obtido}'
    assert obtido == {}, msg
