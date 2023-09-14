import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_posicao
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_posicao')


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'Tempo = {entradas[0]}, Posição = {entradas[1]} e Velocidade = {entradas[2]}')
    for entradas, esperado in [
        ((3, 5, 7), 26),
        ((1234, 6728, 99218), 122441740),
        ((10000, 10000, 10000), 100010000),
    ]
])
def test_valores_inteiros_positivos(entradas, esperado):
    obtido = calcula_posicao(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de Tempo={entradas[0]}, Posição={entradas[1]} e Velocidade={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."

    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'Tempo = {entradas[0]}, Posição = {entradas[1]} e Velocidade = {entradas[2]}')
    for entradas, esperado in [
        ((3.45, 5.85, 7.432), 31.4904),
        ((1454.4224, 6728.31, 99218.123), 144311788.8871552),
        ((10000.966, 10000.9679, 10000.9765), 100029426.911199),
    ]
])
def test_valores_decimais_positivos(entradas, esperado):
    obtido = calcula_posicao(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de Tempo={entradas[0]}, Posição={entradas[1]} e Velocidade={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."

    assert obtido == pytest.approx(esperado), mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'Tempo = {entradas[0]}, Posição = {entradas[1]} e Velocidade = {entradas[2]}')
    for entradas, esperado in [
        ((345, 585, 0), 585),
        ((13, 0, 9), 117),
        ((0, 10, 1342), 10),
        ((0, 1002, 0), 1002),
        ((0, 0, 32), 0),
        ((13, 0, 0), 0),
        ((0, 0, 0), 0),
    ]
])
def test_valores_nulos(entradas, esperado):
    obtido = calcula_posicao(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores de Tempo={entradas[0]}, Posição={entradas[1]} e Velocidade={entradas[2]}. O esperado era {esperado}, mas foi obtido {obtido}."

    assert obtido == pytest.approx(esperado), mensagem
