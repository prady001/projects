import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import extrai_nomes_de_usuarios
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'extrai_nomes_de_usuarios')


def test_emails_do_exemplo():
    lista_emails = ['fulano123@email.com.br', 'bertrano123@gmail.com']
    esperado = ['fulano123', 'bertrano123']
    obtido = extrai_nomes_de_usuarios(lista_emails)
    assert obtido == esperado, f'Não funcionou para a entrada {lista_emails}.\nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_somente_1_email():
    lista_emails = ['fulano123@email.com.br']
    esperado = ['fulano123']
    obtido = extrai_nomes_de_usuarios(lista_emails)
    assert obtido == esperado, f'Não funcionou para a entrada {lista_emails}.\nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_com_email_japones():
    lista_emails = ['ahmano@empresa.com', 'shimano@mail.co.jp']
    esperado = ['ahmano', 'shimano']
    obtido = extrai_nomes_de_usuarios(lista_emails)
    assert obtido == esperado, f'Não funcionou para a entrada {lista_emails}.\nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_somente_3_email_diferentes():
    lista_emails = ['fulano123@email.com.br', 'sicrano@outromail.com', 'beltrano.silva@mail.com.pt']
    esperado = ['fulano123', 'sicrano', 'beltrano.silva']
    obtido = extrai_nomes_de_usuarios(lista_emails)
    assert obtido == esperado, f'Não funcionou para a entrada {lista_emails}.\nEra esperado {esperado}, mas foi obtido {obtido}.'
