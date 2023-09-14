from pathlib import Path
import pytest


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_com_todos_os_meses_do_ano(capsys, mock_input, run_program):
    nome_meses = ['pula_este_aqui','janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    numero_meses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for numero_mes in numero_meses:
        mock_input([numero_mes])
        run_program(program)

        stdout, _ = capsys.readouterr()
        stdout = stdout.strip()
        nome_mes = nome_meses[int(numero_mes)]
        assert stdout == nome_mes, f'Seu programa não imprimiu o esperado: {nome_mes}, ao invés disso imprimiu: {stdout}.'
