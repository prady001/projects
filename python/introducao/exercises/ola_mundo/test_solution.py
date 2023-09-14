from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


def test_imprime_mensagem_diferente_de_ola_mundo(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    assert stdout.strip() != 'Olá mundo!', 'Modifique a mensagem impressa no terminal. Seu programa deve imprimir "Olá NOME" (substituindo NOME pelo seu próprio nome).'
