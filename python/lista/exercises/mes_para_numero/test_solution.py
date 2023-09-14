from pathlib import Path
import pytest


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_com_todos_os_meses_do_ano(capsys, mock_input, run_program):
    nome_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    numero_mes = 1
    for nome_mes in nome_meses:
        mock_input([nome_mes])
        run_program(program)

        stdout, _ = capsys.readouterr()
        stdout = stdout.strip()
        assert stdout == str(numero_mes), f'Seu programa não imprimiu o esperado: {numero_mes}, ao invés disso imprimiu: {stdout}.'
        numero_mes += 1
