import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / "solution.py"


def test_verificando_indentação(capsys, run_program):
    try:
        run_program(program)
    except IndentationError:
        raise IndentationError("Verifique os espaços em branco (indentação) no código para resolver o Erro de Indentação!")

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Você removeu o print do código. Ou a indentação do print está errada.'

    try:
        obtido = int(stdout)
    except ValueError:
        raise AssertionError("O exercício pede para consertar somente a indentação.\nÉ necessário que o código imprima o resultado do seguinte comando x_maior_que_y(10, 5).")

    assert obtido == 1, "O exercício pede para consertar somente a indentação.\nÉ necessário que o código imprima o resultado do seguinte comando x_maior_que_y(10, 5)."
