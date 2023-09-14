import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import nivel_idh
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'nivel_idh')


@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada', [
    pytest.param(entrada, id=f'IDH = {entrada}')
    for entrada in [0.8, 0.9, 1]
])
def test_nível_do_IDH_Muito_Alto(entrada):
    obtido = nivel_idh(entrada)
    esperado = "Muito Alto"
    msg = f'Algo deu errado, para o IDH = {entrada}, era esperado = "{esperado}", mas foi obtido = "{obtido}".'
    if obtido == esperado.lower():
        msg += 'Note que algumas letras devem estar em maiúsculo.'
    assert obtido == esperado, msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada', [
    pytest.param(entrada, id=f'IDH = {entrada}')
    for entrada in [0.7, 0.79]
])
def test_nível_do_IDH_Alto(entrada):
    obtido = nivel_idh(entrada)
    esperado = "Alto"
    msg = f'Algo deu errado, para o IDH = {entrada}, era esperado = "{esperado}", mas foi obtido = "{obtido}".'
    if obtido == esperado.lower():
        msg += 'Note que algumas letras devem estar em maiúsculo.'
    assert obtido == esperado, msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada', [
    pytest.param(entrada, id=f'IDH = {entrada}')
    for entrada in [0.555, 0.556]
])
def test_nível_do_IDH_Médio(entrada):
    obtido = nivel_idh(entrada)
    esperado = "Médio"
    msg = f'Algo deu errado, para o IDH = {entrada}, era esperado = "{esperado}", mas foi obtido = "{obtido}".'
    if obtido == esperado.lower():
        msg += 'Note que algumas letras devem estar em maiúsculo.'
    if obtido in ['medio', 'Medio']:
        msg += 'Veja que a string de retorno possui acento.'
    assert obtido == esperado, msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada', [
    pytest.param(entrada, id=f'IDH = {entrada}')
    for entrada in [0.35, 0.36, 0.554]
])
def test_nível_do_IDH_Baixo(entrada):
    obtido = nivel_idh(entrada)
    esperado = "Baixo"
    msg = f'Algo deu errado, para o IDH = {entrada}, era esperado = "{esperado}", mas foi obtido = "{obtido}".'
    if obtido == esperado.lower():
        msg += 'Note que algumas letras devem estar em maiúsculo.'
    assert obtido == esperado, msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada', [
    pytest.param(entrada, id=f'IDH = {entrada}')
    for entrada in [0.33, 0.1, 0.34]
])
def test_nível_do_IDH_Sem_dados(entrada):
    obtido = nivel_idh(entrada)
    esperado = "Sem dados"
    msg = f'Algo deu errado, para o IDH = {entrada}, era esperado = "{esperado}", mas foi obtido = "{obtido}".'
    if obtido == esperado.lower():
        msg += 'Note que algumas letras devem estar em maiúsculo.'
    assert obtido == esperado, msg
