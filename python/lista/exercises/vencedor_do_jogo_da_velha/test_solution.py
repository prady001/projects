import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import verifica_jogo_da_velha
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'verifica_jogo_da_velha')


@pytest.mark.timeout(5)
def test_vencedor_X():
    tabuleiros = [
        [['X', 'O', 'X'], ['.', 'O', 'X'], ['O', '.', 'X']],
        [['X', 'X', 'X'], ['.', 'O', 'O'], ['O', '.', 'X']],
        [['X', 'O', 'O'], ['.', 'O', 'X'], ['X', 'X', 'X']]
    ]
    for tabu_test in tabuleiros:
        resultado_usuario = verifica_jogo_da_velha(tabu_test)
        tabu_str = ''.join(f'    {linha}\n' for linha in tabu_test)
        assert resultado_usuario == 'X', f'Não funcionou para o tabuleiro\n{tabu_str}\nO resultado esperado era "X", mas foi obtido outro resultado!'


@pytest.mark.timeout(5)
def test_vencedor_O():
    tabuleiros = [
        [['X', 'O', 'O'], ['.', 'O', 'X'], ['O', '.', 'X']],
        [['X', '.', 'X'], ['O', 'O', 'O'], ['.', 'O', 'X']],
        [['O', '.', 'X'], ['X', 'O', 'O'], ['.', 'X', 'O']]
    ]
    for tabu_test in tabuleiros:
        resultado_usuario = verifica_jogo_da_velha(tabu_test)
        tabu_str = ''.join(f'    {linha}\n' for linha in tabu_test)
        assert resultado_usuario == 'O', f'Não funcionou para o tabuleiro\n{tabu_str}\nO resultado esperado era "O", mas foi obtido outro resultado!'


@pytest.mark.timeout(5)
def test_sem_vencedor():
    tabuleiros = [
        [['X', '.', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O']],
        [['O', '.', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']],
        [['O', 'X', 'O'], ['X', 'O', 'X'], ['X', 'O', 'X']]
    ]
    for tabu_test in tabuleiros:
        resultado_usuario = verifica_jogo_da_velha(tabu_test)
        tabu_str = ''.join(f'    {linha}\n' for linha in tabu_test)
        assert resultado_usuario == 'V', f'Não funcionou para o tabuleiro\n{tabu_str}\nO resultado esperado era "V", mas foi obtido outro resultado!'
