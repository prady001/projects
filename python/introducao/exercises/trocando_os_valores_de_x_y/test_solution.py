import variaveis

from pytest_devlife import util
try:
    import solution
except:
    solution = None


def setup():
    if not solution:
        raise AssertionError('Erro ao carregar a solução. Verifique a syntaxe do código.')


def test_trocando_os_valores_de_x_y():
    mensagem = "Algo deu errado. "
    if solution.x != variaveis.y and solution.y != variaveis.x:
        mensagem+= f"Era esperado que a variável x armazenasse o valor {variaveis.y}, porém o valor {solution.x} foi obtido.\n"
        mensagem+= f"Era esperado que a variável y armazenasse o valor {variaveis.x}, porém o valor {solution.y} foi obtido.\n"
    elif solution.x != variaveis.y:
        mensagem+= f"Era esperado que a variável x armazenasse o valor {variaveis.y}, porém o valor {solution.x} foi obtido.\n"
    else:
        mensagem+= f"Era esperado que a variável y armazenasse o valor {variaveis.x}, porém o valor {solution.y} foi obtido.\n"

    assert solution.x == variaveis.y and solution.y == variaveis.x, mensagem
