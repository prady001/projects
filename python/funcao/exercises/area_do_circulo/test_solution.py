import pytest
from math import pi
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_area_do_circulo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_area_do_circulo')


@pytest.mark.parametrize("raio, area", [
    pytest.param(raio, area, id=f'Raio: {raio}')
    for raio, area in [
        (1, pi*1**2),
        (2, pi*2**2),
        (3, pi*3**2),
        (4, pi*4**2),
        (5, pi*5**2),
        (6, pi*6**2),
        (7, pi*7**2),
        (8, pi*8**2)
    ]])
def test_vários_raios(raio, area):
    dica = ''
    saida = calcula_area_do_circulo(raio)
    if type(saida) != type(area):
        dica += f'O tipo da resposta esperado é {type(area)}, mas sua função devolve {type(saida)}.'
    assert area == saida, f'Algo deu errado. \nAo calcular a área para o raio {raio}, esperava {area} mas obteve {saida}.\n{dica}'
