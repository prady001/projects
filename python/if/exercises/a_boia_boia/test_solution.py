import pytest
import math
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import vai_boiar
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'vai_boiar')


def test_boia_menos_densa_que_agua():
    peso = 10
    raio_maior = 60
    raio_menor = 3
    densidade_esperada = 938.15
    obtido = vai_boiar(peso, raio_maior, raio_menor)
    esperado = True
    assert obtido == esperado, f'Algo deu errado com o peso = {peso}, raio_maior = {raio_maior} e raio_menor = {raio_menor}. Era esperado {esperado}, mas foi obtido {obtido}, a densidade_esperada testada é aproximadamente {densidade_esperada} kg/m³ ou {densidade_esperada/1000:.3f} g/cm³, cheque se está usando as unidades corretas.'


def test_boia_mais_densa_que_agua():
    peso = 10
    raio_maior = 50
    raio_menor = 3
    densidade_esperada = 1125.79
    obtido = vai_boiar(peso, raio_maior, raio_menor)
    esperado = False
    assert obtido == esperado, f'Algo deu errado com o peso = {peso}, raio_maior = {raio_maior} e raio_menor = {raio_menor}. Era esperado {esperado}, mas foi obtido {obtido}, a densidade_esperada testada é aproximadamente {densidade_esperada} kg/m³ ou {densidade_esperada/1000:.3f} g/cm³, cheque se está usando as unidades corretas.'


def test_boia_com_mesma_densidade_de_agua():
    peso = 997*2
    raio_maior = 1/math.pi**2
    raio_menor = 1000
    obtido = vai_boiar(peso, raio_maior, raio_menor)
    esperado = True
    assert obtido == esperado, f'algo deu errado. Era esperado {esperado}, mas foi obtido {obtido}, a densidade_esperada testada é 997 kg/m³ ou 0.997 g/cm³, cheque se está usando as unidades corretas.'
