import pytest
import random
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import apostando_em_dados
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'apostando_em_dados')


@pytest.mark.timeout(5)
@pytest.mark.parametrize('numero_da_sorte, aposta, rodadas, esperado', [
    pytest.param(numero_da_sorte, aposta, rodadas, esperado, id=f'numero da sorte = {numero_da_sorte}, aposta = {aposta} e rodadas = {rodadas}')
    for numero_da_sorte, aposta, rodadas, esperado in [
        (1, 100, 1, 83.33333333333334),
        (1, 150, 2, 166.66666666666666),
        (1, 155, 3, 229.62962962962962),
        (2, 200, 4, 96.45061728395063),
        (2, 210, 5, 84.3942901234568),
        (2, 215, 6, 115.20490397805216),
        (3, 216, 7, 96.45061728395062),
        (3, 219, 8, 81.4918409922268),
        (3, 220, 9, 68.21995821267085),
        (4, 250, 10, 40.376395722461446),
        (4, 255, 11, 34.319936364092236),
        (4, 300, 12, 33.64699643538454),
        (5, 300, 13, 44.86266191384605),
        (5, 310, 14, 38.63173664803412),
        (5, 315, 15, 52.339772232820394),
        (6, 1000, 16, 567.1526641947944),
        (6, 5000, 17, 2363.1361008116432),
        (6, 10000, 18, 3938.5601680194054),
    ]
])
def test_apostando_em_dados(numero_da_sorte, aposta, rodadas, esperado):
    random.seed(42)
    sorteios = [6, 1, 1, 6, 3, 2, 2, 2, 6, 1, 6, 6, 5, 1, 5, 4, 1, 1]
    obtido = apostando_em_dados(numero_da_sorte, aposta, rodadas)

    assert obtido == pytest.approx(esperado), f'Algo deu errado! Não funcionou para {sorteios[:rodadas].count(numero_da_sorte)} sorteios de {len(sorteios[:rodadas])} rodadas.'
