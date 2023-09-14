import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import eh_bissexto
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'eh_bissexto')



@pytest.mark.parametrize(
    'ano',
    [1999,1997,1995,1993,1991,1989,1987]
)
def test_ano_nao_eh_multiplo_4(ano):
    resultado = eh_bissexto(ano)
    dica = 'Lembre-se pesquisar sobre o critério classificação de bissexto ou não.'
    assert resultado == False, f'Algo deu errado na hora de verificar se {ano} é bissexto.\n{dica}'


@pytest.mark.parametrize(
    'ano',
    [2020,2016,2012,2008,2004,1996,1992]
)
def test_ano_eh_multiplo_4_somente(ano):
    resultado = eh_bissexto(ano)
    dica = 'Lembre-se de que, para ser bissexto, o ano deve ser divisível por 4.'
    assert resultado == True, f'Algo deu errado na hora de verificar se {ano} é bissexto.\n{dica}'


@pytest.mark.parametrize(
    'ano',
    [1900,1800,1700,1500,1400,1300,1100]
)
def test_ano_eh_multiplo_100_mas_nao_400(ano):
    resultado = eh_bissexto(ano)
    dica = 'Lembre-se de que, para ser bissexto, o ano não pode ser divisível por 100, a menos que seja divisível por 4 também.'
    assert resultado == False, f'Algo deu errado na hora de verificar se {ano} é bissexto.\n{dica}'


@pytest.mark.parametrize(
    'ano',
    [2800,2400,2000,1600,1200,800,400]
)
def test_ano_eh_multiplo_400(ano):
    resultado = eh_bissexto(ano)
    dica = 'Lembre-se de que se um ano é divisível por 400, ele é bissexto.'
    assert resultado == True, f'Algo deu errado na hora de verificar se {ano} é bissexto.\n{dica}'
