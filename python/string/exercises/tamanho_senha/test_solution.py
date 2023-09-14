import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import tamanho_minimo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'tamanho_minimo')


def test_argumento_do_exemplo():
    n = 5
    possiveis_senhas = 'frase pra testar se a função filtra as palavras'
    lista_senhas = ['testar', 'função', 'filtra', 'palavras']
    resultado = tamanho_minimo(possiveis_senhas, n)
    assert resultado == lista_senhas, f'Algo deu errado na hora de filtrar as senhas com mais de {n} caracteres de {possiveis_senhas}.\nEra esperado {lista_senhas}, mas foi obtido {resultado}.'


def test_n_maior_que_todas_palavras():
    n = 30
    possiveis_senhas = 'godspeed flash kid_flash capitao_frio capitao_bumerangue patinadora_dourada flash_reverso'
    lista_senhas = []
    resultado = tamanho_minimo(possiveis_senhas, n)
    assert resultado == lista_senhas, f'Algo deu errado na hora de filtrar as senhas com mais de {n} caracteres de {possiveis_senhas}.\nEra esperado {lista_senhas}, mas foi obtido {resultado}.'


def test_n_menor_que_todas_palavras():
    n = 4
    possiveis_senhas = 'godspeed flash kid_flash capitao_frio capitao_bumerangue patinadora_dourada flash_reverso'
    lista_senhas = ['godspeed', 'flash', 'kid_flash', 'capitao_frio', 'capitao_bumerangue', 'patinadora_dourada', 'flash_reverso']
    resultado = tamanho_minimo(possiveis_senhas, n)
    assert resultado == lista_senhas, f'Algo deu errado na hora de filtrar as senhas com mais de {n} caracteres de {possiveis_senhas}.\nEra esperado {lista_senhas}, mas foi obtido {resultado}.'


def test_n_maior_que_algumas_palavras_e_menor_que_outras():
    n = 4
    possiveis_senhas = 'NO DIA MAIS CLARO NA NOITE MAIS DENSA'
    lista_senhas = ['CLARO', 'NOITE', 'DENSA']
    resultado = tamanho_minimo(possiveis_senhas, n)
    assert resultado == lista_senhas, f'Algo deu errado na hora de filtrar as senhas com mais de {n} caracteres de {possiveis_senhas}.\nEra esperado {lista_senhas}, mas foi obtido {resultado}.'


def test_nenhuma_palavra_string_vazia():
    n = 1
    possiveis_senhas = ''
    lista_senhas = []
    resultado = tamanho_minimo(possiveis_senhas, n)
    assert resultado == lista_senhas, f'Algo deu errado na hora de filtrar as senhas com mais de {n} caracteres de {possiveis_senhas}.\nEra esperado {lista_senhas}, mas foi obtido {resultado}.'
