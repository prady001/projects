import pytest
import pprint
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import filtra_bagagens
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'filtra_bagagens')


@pytest.mark.timeout(5)
@pytest.mark.parametrize("bagagens, altura, largura, profundidade, esperado", [
    pytest.param(bagagens, altura, largura, profundidade, esperado,
                 id=f'{pprint.pformat(bagagens)}')
    for bagagens, altura, largura, profundidade, esperado in [
        ([[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0],
         [50.3, 30.2, 30.0], [54.0, 30.2, 22.1]], 55, 35, 25, 2),
        ([[15.0, 12.8, 10.2], [20.0, 15.0, 14.0]], 20, 15, 14, 0),
        ([[20, 18, 15], [20, 20, 20]], 19, 17, 16, 2),
        ([[45, 39, 35], [50, 40, 30], [60, 35, 25], [45, 44, 30]], 50, 40, 30, 3),
        ([[100.2, 90.3, 80.1]], 50, 50, 50, 1),
        ([], 100, 50, 30, 0),
    ]])
def test_várias_bagagens(bagagens, altura, largura, profundidade, esperado):
    dica = ''
    saida = filtra_bagagens(bagagens, altura, largura, profundidade)
    if type(saida) != type(esperado):
        dica += f'Esperava uma resposta do tipo {type(esperado)}, mas obteve {type(saida)}. Verifique o tipo da resposta de sua função.'
    else:
        dica += f'Lembre-se da ordem dos argumentos que a função recebe! \nOrdem:`<lista com as bagagens>, <altura>, <largura>, <profundidade>`'
    assert esperado == saida, f'Algo deu errado. \nPara a entrada {pprint.pformat(bagagens)}, era esperado {esperado} mas obteve {saida}.\n\n{dica}\n'
