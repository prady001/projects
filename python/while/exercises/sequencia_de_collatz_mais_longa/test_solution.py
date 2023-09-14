from pathlib import Path
import pytest


PWD = Path(__file__).parent
program = PWD / "solution.py"


@pytest.mark.timeout(5)
def test_n_1(capsys, mock_input, run_program):
    mock_input(['1'])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nenhum valor.'

    try:
        obtido = int(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor n que gera a maior sequência e nada mais.')

    assert obtido == 1, f'Com n=1 só temos um elemento: o 1. Sua resposta foi {stdout}'


@pytest.mark.timeout(5)
def test_n_4(capsys, mock_input, run_program):
    mock_input(['4'])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nenhum valor.'

    try:
        obtido = int(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor n que gera a maior sequência e nada mais.')
    assert obtido == 3, f'Com n=4 a resposta esperada é 3. Sua resposta foi {stdout}'


@pytest.mark.timeout(5)
def test_n_1000(capsys, mock_input, run_program):
    mock_input(['1000'])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nenhum valor.'

    try:
        obtido = int(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor n que gera a maior sequência e nada mais.')
    assert obtido == 871, f'Com n=1000 a resposta esperada é 871. Sua resposta foi {stdout}'
