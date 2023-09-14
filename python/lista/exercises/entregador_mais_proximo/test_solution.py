import pytest
from pprint import pformat
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import entregador_mais_proximo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'entregador_mais_proximo')


testes = [
    (([3, 4],[[10, 20], [4, 2], [100, 74], [23, 63]]), 1),
    (([3, 4],[[3, 4], [4, 2], [100, 74], [23, 63]]), 0),
    (([3, 4],[[10, 20], [4, 2], [4, 4], [23, 63]]), 2),
    (([3, 4],[[10, 20], [4, 2], [100, 74], [4, 3]]), 3),
    (([15, 20], [[28, 4], [63, 87], [192, 643], [16, 19], [523, 32]]), 3),
    (([123, 654], [[1244, 432]]), 0),
    (([0, 0], [[123, 432], [42, 312], [10, 20]]), 2),
]


@pytest.mark.timeout(5)
@pytest.mark.parametrize("restaurante, entregadores, esperado", [
    pytest.param(testes[i][0][0], testes[i][0][1], testes[i][1], id=f'ENTRADA{i}') for i in range(len(testes))
])
def test_lista_pra_varias_entradas(restaurante, entregadores, esperado):
    dica = f''
    saida = entregador_mais_proximo(restaurante, entregadores)
    if type(saida) != type(esperado):
        dica += f'Verifique se sua função retorna um inteiro'

    assert saida == esperado, f'Algo deu errado. Para as cordenadas do restaurante: {pformat(restaurante)}; e para as cordenadas dos entregadores: {pformat(entregadores)}; obteve {saida} mas esperava {esperado}.\nLembre-se de usar a fórmula dada no enunciado.\n{dica}'
