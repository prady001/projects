import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_investimento
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_investimento')


@pytest.mark.timeout(5)
@pytest.mark.parametrize('investimento_inicial, numero_de_meses, ativo, esperado', [
    pytest.param(investimento_inicial, numero_de_meses, ativo, esperado, id=f'investimento inicial = {investimento_inicial}, meses = {numero_de_meses}, ativo = {ativo}')
    for investimento_inicial, numero_de_meses, ativo, esperado in [
        (1000, 10, 'LCA', 1178.0487458407313),
        (1000, 12, 'LCA', 1224.5844426611145),
        (1000, 3, 'LCA', 1044.1337986249998),
        (5000, 36, 'LCA', 9181.977361806425),
        (650, 15, 'LCA', 831.1095038043386),
        (1200, 36, 'LCA', 2203.6745668335407),
        (500, 15, 'LCA', 639.315002926414),
        (1200, 17, 'LCA', 1594.9666788733239),
        (10000, 38, 'LCA', 18900.370432078256),
    ]
])
def test_investindo_em_LCA(investimento_inicial, numero_de_meses, ativo, esperado):
    obtido = calcula_investimento(investimento_inicial, numero_de_meses, ativo)
    assert obtido == pytest.approx(esperado), f'Algo deu errado, para o investimento inicial = {investimento_inicial}, número de meses = {numero_de_meses} e ativo = {ativo}. Era esperado {esperado}, porém foi obtido {obtido}.'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('investimento_inicial, numero_de_meses, ativo, esperado', [
    pytest.param(investimento_inicial, numero_de_meses, ativo, esperado, id=f'investimento inicial = {investimento_inicial}, meses = {numero_de_meses}, ativo = {ativo}')
    for investimento_inicial, numero_de_meses, ativo, esperado in [
        (1000, 12, 'LCI', 1209.8304065090824),
        (5000, 25, 'LCI', 7435.543231570764),
        (10000, 13, 'LCI', 12291.87693013227),
        (1000, 32, 'LCI', 1661.8761466711096),
        (20000, 29, 'LCI', 31691.845216124213),
        (1000, 14, 'LCI', 1248.8546961014395),
        (5000, 32, 'LCI', 8309.380733355541),
        (20000, 46, 'LCI', 41508.83660218353),
    ]
])
def test_investindo_em_LCI(investimento_inicial, numero_de_meses, ativo, esperado):
    obtido = calcula_investimento(investimento_inicial, numero_de_meses, ativo)
    assert obtido == pytest.approx(esperado), f'Algo deu errado, para o investimento inicial = {investimento_inicial}, número de meses = {numero_de_meses} e ativo = {ativo}. Era esperado {esperado}, porém foi obtido {obtido}.'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('investimento_inicial, numero_de_meses, ativo, esperado', [
    pytest.param(investimento_inicial, numero_de_meses, ativo, esperado, id=f'investimento inicial = {investimento_inicial}, meses = {numero_de_meses}, ativo = {ativo}')
    for investimento_inicial, numero_de_meses, ativo, esperado in [
        (1000, 12, 'CDB', 1195.8435607553713),
        (1000, 18, 'CDB', 1307.7103288612934),
        (1000, 25, 'CDB', 1448.6323654834862),
        (10000, 14, 'CDB', 12271.37590896778),
        (650, 2, 'CDB', 667.0098499999999),
        (1000, 22, 'CDB', 1377.0488137434302),
    ]
])
def test_investindo_em_CDB(investimento_inicial, numero_de_meses, ativo, esperado):
    obtido = calcula_investimento(investimento_inicial, numero_de_meses, ativo)
    assert obtido == pytest.approx(esperado), f'Algo deu errado, para o investimento inicial = {investimento_inicial}, número de meses = {numero_de_meses} e ativo = {ativo}. Era esperado {esperado}, porém foi obtido {obtido}.'
