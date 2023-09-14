import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import quantos_uns
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'quantos_uns')


@pytest.mark.parametrize('numero, quant_uns', [
    pytest.param(1023418932, 2, id='numero=1023418932'),
    pytest.param(1901913190122, 5, id='numero=1901913190122'),
    pytest.param(213123980121, 4, id='numero=213123980121')
])
@pytest.mark.timeout(5)
def test_numeros_com_variados_uns(numero, quant_uns):
    resultado = quantos_uns(numero)
    assert resultado == quant_uns, f'Algo deu errado!\nEra esperado {quant_uns}, mas retornou {resultado}!'


@pytest.mark.parametrize('numero, quant_uns', [
    pytest.param(1, 1, id='numero=1'),
    pytest.param(12, 1, id='numero=12'),
    pytest.param(210, 1, id='numero=210')
])
@pytest.mark.timeout(5)
def test_numeros_de_1_a_3_algarismos(numero, quant_uns):
    resultado = quantos_uns(numero)
    assert resultado == quant_uns, f'Algo deu errado!\nEra esperado {quant_uns}, mas retornou {resultado}!'


@pytest.mark.parametrize('numero, quant_uns', [
    pytest.param(-13920183021, 3, id='numero=-13920183021'),
    pytest.param(-38912312, 2, id='numero=-38912312'),
    pytest.param(-38912311211, 5, id='numero=-38912311211')
])
@pytest.mark.timeout(5)
def test_numeros_negativos(numero, quant_uns):
    resultado = quantos_uns(numero)
    assert resultado == quant_uns, f'Algo deu errado!\nEra esperado {quant_uns}, mas retornou {resultado}!'


@pytest.mark.parametrize('numero, quant_uns', [
    pytest.param(-2357623487, 0, id='numero=-2357623487'),
    pytest.param(523986235, 0, id='numero=523986235'),
])
@pytest.mark.timeout(5)
def test_numeros_sem_um(numero, quant_uns):
    resultado = quantos_uns(numero)
    assert resultado == quant_uns, f'Algo deu errado!\nEra esperado {quant_uns}, mas retornou {resultado}!'
