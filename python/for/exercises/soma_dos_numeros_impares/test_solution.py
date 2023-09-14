import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import soma_impares
except:
    pass

def setup():
    util.function_exists_in_module(solution, 'soma_impares')


gabarito = [([74, 92, 2, 91, 98, 56, 52, 9, 30, 58], 100), ([74, 68, 5, 20, 32, 75, 15, 75, 96, 59, 59, 96, 25, 28, 61, 21, 42, 68, 54, 64], 395), ([65, 28, 58, 48, 82, 91, 65, 58, 43, 59, 43, 54, 47, 51, 46, 6, 32, 43, 78, 81, 35, 64, 51, 30, 45, 47, 36, 99, 85, 46], 950), ([94, 38, 32, 90, 76, 32, 14, 54, 24, 39, 57, 95, 22, 33, 87, 38, 82, 65, 49, 76, 68, 97, 85, 25, 1, 11, 94, 46, 58, 27, 53, 95, 7, 74, 96, 40, 56, 70, 40, 99], 925), ([47, 10, 18, 43, 27, 30, 28, 6, 86, 35, 34, 86, 64, 71, 49, 71, 8, 38, 28, 7, 12, 43, 14, 21, 45, 30, 72, 42, 58, 48, 83, 96, 18, 58, 82, 12, 13, 61, 95, 49, 92, 87, 24, 6, 73, 75, 9, 99, 87, 33], 1223), ([29, 85, 26, 14, 58, 66, 95, 70, 55, 70, 48, 68, 13, 32, 84, 24, 35, 75, 61, 33, 44, 58, 89, 47, 48, 88, 74, 95, 71, 30, 99, 8, 56, 70, 35, 42, 28, 5, 47, 85, 99, 44, 5, 85, 76, 29, 90, 42, 42, 6, 31, 69, 29, 16, 8, 57, 40, 8, 96, 55], 1513), ([6, 88, 69, 9, 7, 19, 36, 49, 3, 58, 97, 69, 9, 18, 76, 83, 30, 53, 93, 65, 69, 3, 88, 77, 20, 11, 82, 81, 99, 17, 37, 92, 24, 25, 35, 30, 58, 16, 0, 84, 24, 44, 36, 29, 13, 25, 76, 66, 32, 27, 49, 39, 81, 77, 94, 97, 94, 65, 10, 61, 87, 15, 51, 1, 80, 81, 41, 83, 7, 14], 2008), ([50, 57, 95, 57, 16, 80, 9, 41, 82, 95, 60, 28, 26, 15, 43, 82, 36, 96, 19, 11, 72, 45, 35, 36, 99, 33, 41, 47, 17, 87, 46, 29, 33, 82, 80, 68, 16, 5, 83, 99, 23, 76, 84, 46, 27, 39, 66, 59, 19, 51, 45, 47, 93, 79, 68, 80, 95, 31, 55, 14, 2, 19, 30, 0, 19, 79, 5, 28, 14, 6, 84, 96, 61, 84, 43, 8, 27, 17, 95, 70], 2123)]


def test_lista_vazia():
    resultado_obtido = soma_impares([])
    assert resultado_obtido == 0, f'Não funcionou para lista vazia.'


@pytest.mark.parametrize(
    'lista, resultado_esperado',
    [
        pytest.param(
            lista,
            resultado_esperado,
            id=f'lista: {lista}; resultado esperado: {resultado_esperado}'
        )
        for lista, resultado_esperado in gabarito
    ]
)
def test_lista_de_numeros_aleatorios(lista, resultado_esperado):
    resultado_obtido = soma_impares(lista)
    msg = f'Não funcionou para a lista {lista}. Era esperado {resultado_esperado}, foi obtido {resultado_obtido}'
    assert resultado_obtido == resultado_esperado, msg
