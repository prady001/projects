import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import classifica_caixa
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'classifica_caixa')


@pytest.mark.timeout(5)
@pytest.mark.parametrize('comprimento, peso', [
    pytest.param(comprimento, peso, id=f'comprimento = {comprimento}, peso = {peso}')
    for comprimento, peso in [
        (10, 10),
        (15, 10),
        (20, 10),
        (25, 30),
        (30, 40),
        (35, 20),
        (40, 20),
        (45, 20),
        (50, 50),
        (55, 10),
        (60, 10),
        (65, 30),
        (70, 50),
    ]
])
def test_caixa_com_legume(comprimento, peso):
    obtido = classifica_caixa(comprimento, peso)
    msg = f'Algo deu errado, para os valores comprimento = {comprimento} e peso = {peso} a função deveria retornar "legume", porém retornou "{obtido}" '

    if obtido.lower() == 'legume':
        msg+= '\nVerifique se todas as letras estão escritas em letras minúsculas.'
    if obtido.lower() == 'legumes':
        msg+= '\nVeja que a função deve retorna a string no singular.'

    assert obtido == 'legume', msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('comprimento, peso', [
    pytest.param(comprimento, peso, id=f'comprimento = {comprimento}, peso = {peso}')
    for comprimento, peso in [
        (10, 30),
        (10, 40),
        (10, 50),
        (15, 30),
        (15, 40),
        (15, 50),
        (20, 40),
        (20, 50),
        (25, 40),
        (25, 50),
        (30, 50),
        (35, 50),
        (40, 50),
    ]
])
def test_caixa_com_verdura(comprimento, peso):
    obtido = classifica_caixa(comprimento, peso)
    msg = f'Algo deu errado, para os valores comprimento = {comprimento} e peso = {peso} a função deveria retornar "verdura", porém retornou "{obtido}" '

    if obtido.lower() == 'verdura':
        msg+= '\nVerifique se todas as letras estão escritas em letras minúsculas.'
    if obtido.lower() == 'verduras':
        msg+= '\nVeja que a função deve retorna a string no singular.'

    assert obtido == 'verdura', msg
