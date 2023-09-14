import pytest
from pytest import approx
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_programa_para_quando_digita_0(capsys, mock_input, run_program):
    mock_input([str(0), str(1)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu a soma dos números.'

    try:
        captured = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor da soma e nada mais.')

    assert captured == 0, f'Algo deu de errado, seu programa não somou os valores inseridos corretamente. Era esperado 0, porém foi obtido {captured}.'


@pytest.mark.timeout(5)
def test_programa_soma_corretamente_valores(capsys, mock_input, run_program):
    mock_input([str(1), str(1), str(4), str(0)])
    try:
        run_program(program)
    except BaseException as e:
        if "Failed" in str(type(e)):
            raise AssertionError('Algo deu de errado, seu programa não parou quando recebeu "0" como input.')
        else:
            raise e

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu a soma dos números.'
    try:
        captured = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor da soma e nada mais.')
    assert captured == 6, f'Algo deu de errado, seu programa não somou os valores inseridos corretamente. Era esperado 6, porém foi obtido {captured}.'


@pytest.mark.timeout(5)
def test_programa_soma_corretamente_valores_float(capsys, mock_input, run_program):
    mock_input([str(0.1), str(0.2), str(0.3), str(0)])
    try:
        run_program(program)
    except BaseException as e:
        if "Failed" in str(type(e)):
            raise AssertionError('Algo deu de errado, seu programa não parou quando recebeu "0" como input.')
        else:
            raise e

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu a soma dos números.'
    try:
        captured = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor da soma e nada mais.')
    assert captured == approx(0.6), f'Algo deu de errado, seu programa não somou os valores com casas decimais inseridos corretamente. Era esperado 0.6, mas foi obtido {captured}.'


@pytest.mark.timeout(5)
def test_programa_soma_corretamente_valores_negativos(capsys, mock_input, run_program):
    mock_input([str(1), str(1), str(-4), str(0)])
    try:
        run_program(program)
    except BaseException as e:
        if "Failed" in str(type(e)):
            raise AssertionError('Algo deu de errado, seu programa não parou quando recebeu "0" como input.')
        else:
            raise e

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu a soma dos números.'
    try:
        captured = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor da soma e nada mais.')
    assert captured == -2, f'Algo deu de errado, seu programa não somou os valores inseridos corretamente. Era esperado -2, porém foi obtido {captured}.'
