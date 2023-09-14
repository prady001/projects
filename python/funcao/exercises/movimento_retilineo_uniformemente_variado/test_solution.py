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
                 id=f'posição inicial = {entradas[0]}, velocidade inicial = {entradas[1]}, aceleração = {entradas[2]} e tempo decorrido = {entradas[3]}')
    for entradas, esperado in [
        ((50, 100, 0, 0), 50),
        ((0, 100, 0, 10), 1000),
        ((500, 0, 0, 10), 500),
        ((50, 100, 0, 10), 1050),
        ((50, 100, 10, 10), 1550),
    ]
])
def test_valores_inteiros(entradas, esperado):
    obtido = calcula_posicao(entradas[0], entradas[1], entradas[2], entradas[3])
    mensagem = f"Algo deu errado ao testar os valores {entradas}. O esperado era {esperado}, mas foi obtido {obtido}.\nVerifique se os argumentos da função estão na ordem correta.\nVerifique também se a fórmula para o cálculo está correto."

    assert obtido == esperado, mensagem


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'posição inicial = {entradas[0]}, velocidade inicial = {entradas[1]}, aceleração = {entradas[2]} e tempo decorrido = {entradas[3]}')
    for entradas, esperado in [
        ((1.123, 2.345, 3.2, 3.234), 25.4407396),
        ((50, 100.5, 0.5, 0.9), 140.65249999999997),
        ((0, 100.3, 0, 10), 1003.0),
        ((500.5, 0, 0, 10), 500.5),
        ((50, 100, 0, 10.14), 1064.0),
        ((50, 100, 10.4, 10), 1570.0),
    ]
])
def test_valores_decimas(entradas, esperado):
    obtido = calcula_posicao(entradas[0], entradas[1], entradas[2], entradas[3])
    mensagem = f"Algo deu errado ao testar os valores {entradas}. O esperado era {esperado}, mas foi obtido {obtido}.\nVerifique se os argumentos da função estão na ordem correta.\nVerifique também se a fórmula para o cálculo está correto."

    assert obtido == pytest.approx(esperado), mensagem


def test_zero_para_todos_os_argumentos():
    obtido = calcula_posicao(0, 0, 0, 0)
    mensagem = f"Algo deu errado ao testar calcula_posicao(0, 0, 0, 0). O esperado era 0, mas foi obtido {obtido}."

    assert obtido == 0, mensagem
