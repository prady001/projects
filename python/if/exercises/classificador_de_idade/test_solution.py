import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import classifica_idade
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'classifica_idade')


@pytest.mark.parametrize('idade', range(1,12))
def test_crianca(idade):
    esperado = 'crianca'
    obtido = classifica_idade(idade)
    msg_extra = ''
    if idade == 11:
        msg_extra = f' Uma pessoa de 11 anos é considerada criança e não {obtido}.\n'
    if obtido == "criança":
        msg_extra+= 'Perceba que o exercício pede a palavra "crianca" sem "ç"'
    assert obtido == esperado, f'Era esperado "{esperado}" e foi recebido "{obtido}".{msg_extra}'


@pytest.mark.parametrize('idade', range(12,18))
def test_adolescente(idade):
    esperado = 'adolescente'
    obtido = classifica_idade(idade)
    msg_extra = ''
    if idade == 12:
        msg_extra = f' Uma pessoa de 12 anos é considerada adolescente e não {obtido}.'
    elif idade == 17:
        msg_extra = f' Uma pessoa de 17 anos é considerada adolescente e não {obtido}.'
    assert obtido == esperado, f'Era esperado "{esperado}" e foi recebido "{obtido}".{msg_extra}'


@pytest.mark.parametrize('idade', range(18,29))
def test_adulto(idade):
    esperado = 'adulto'
    obtido = classifica_idade(idade)
    msg_extra = ''
    if idade == 18:
        msg_extra = f' Uma pessoa de 18 anos é considerada adulta e não {obtido}.'
    assert obtido == esperado, f'Era esperado "{esperado}" e foi recebido "{obtido}".{msg_extra}'
