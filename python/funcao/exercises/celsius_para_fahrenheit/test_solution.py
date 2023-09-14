import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import celsius_para_fahrenheit
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'celsius_para_fahrenheit')



lista_celsius = [0, 12, 25, 34, 53, 66, 78, 89, 96, 102]
lista_fahrenheit = [32, 53.6, 77, 93.2, 127.4, 150.8, 172.4, 192.2, 204.8, 215.6]

@pytest.mark.parametrize(
    'celsius, fahrenheit',
    [
        pytest.param(i, j, id=f'celsius={i} fahrenheit={j}') for i, j in zip(lista_celsius, lista_fahrenheit)
    ]
)
def test_celsius_para_fahrenheit(celsius, fahrenheit):
    obtido = celsius_para_fahrenheit(celsius)
    assert obtido == pytest.approx(fahrenheit), f'Algo deu errado na conversão da temperatura {celsius} celsius em fahrenheit.\nEra esperado {fahrenheit}, mas foi obtido {obtido}.'


lista_neg_celsius = [-200, -164, -142, -120, -100, -86, -50, -32, -15, -1]
lista_neg_fahrenheit = [-328.0, -263.2, -223.6, -184.0, -148.0, -122.8, -58.0, -25.6, 5.0, 30.2]

@pytest.mark.parametrize(
    'celsius, fahrenheit',
    [
        pytest.param(k, m, id=f'celsius={k} fahrenheit={m}') for k, m in zip(lista_neg_celsius, lista_neg_fahrenheit)
    ]
)
def test_temperatura_negativa(celsius, fahrenheit):
    obtido = celsius_para_fahrenheit(celsius)
    assert obtido == pytest.approx(fahrenheit), f'Sua conversão não funcionou para o valor negativo {celsius}.\nEra esperado {fahrenheit}, mas foi obtido {obtido}.'


def test_temperatura_bem_alta():
    obtido = celsius_para_fahrenheit(133495)
    assert obtido == pytest.approx(240323), f'Algo deu errado na conversão da temperatura 133495 celsius em fahrenheit.\nEra esperado 240323, mas foi obtido {obtido}.'
