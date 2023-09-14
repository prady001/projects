import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_idade
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_idade')


@pytest.mark.parametrize("parametros, esperado", [
    pytest.param(parametros, esperado,
                 id=f'Nascimento: {parametros[0]}/{parametros[1]}/{parametros[2]}. Atual: {parametros[3]}/{parametros[4]}/{parametros[5]}')
    for parametros, esperado in [
        ([14, 2, 1989, 15, 1, 2021], 31),
        ([14, 2, 1989, 13, 2, 2021], 31),
        ([14, 2, 1989, 14, 2, 2021], 32),
        ([14, 2, 1989, 15, 2, 2021], 32),
        ([14, 2, 1989, 13, 3, 2021], 32)
    ]])
def test_diferentes_datas_atuais(parametros, esperado):
    dica = ''
    saida = calcula_idade(*parametros)
    if type(saida) != type(esperado):
        dica += f'É esperado que a saída de sua função seja um númemo inteiro. Recebeu {type(saida)}'
    else:
        if esperado > saida:
            dica += f'A idade obtida por sua função é MENOR que esperado.'
        elif saida > esperado:
            dica += f'A idade obtida por sua função é MAIOR que esperado.'
    assert esperado == saida, f'Algo deu errado. \nEsperava {esperado}, mas obteve {saida}. \n\n{dica}'
