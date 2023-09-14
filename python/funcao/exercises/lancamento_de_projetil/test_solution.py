import pytest
import math
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_distancia_do_projetil
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_distancia_do_projetil')


@pytest.mark.parametrize('entradas, esperado', [
    pytest.param(entradas, esperado,
                 id=f'velocidade = {entradas[0]}, ângulo = {entradas[1]} e altura = {entradas[2]}')
    for entradas, esperado in [
        ((math.sqrt(9.8), math.pi / 6, 1), 1.7320508075688772),
        ((20, math.pi / 4, 1), 41.792958199885284),
        ((30, math.pi / 3, 1), 80.10616414615706)
    ]
])
def test_valores_inteiros(entradas, esperado):
    obtido = calcula_distancia_do_projetil(entradas[0], entradas[1], entradas[2])
    mensagem = f"Algo deu errado ao testar os valores {entradas}. O esperado era {esperado}, mas foi obtido {obtido}.\nVerifique se os argumentos da função estão na ordem correta.\nVerifique também se a fórmula para o cálculo está correto."

    assert obtido == pytest.approx(esperado), mensagem
