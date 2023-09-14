from pathlib import Path
import pytest


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_do_exemplo(capsys, mock_input, run_program):
    entradas = ['1', '4', '2', '6', '3', '0']
    lista_esperada = ['0', '3', '6', '2', '4', '1']
    mock_input(entradas)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.split('\n')
    stdout.remove('')
    assert stdout == lista_esperada, f'Seu programa não imprimiu o esperado: {lista_esperada}, ao invés disso imprimiu: {stdout}.'


@pytest.mark.timeout(5)
def test_numeros_grandes(capsys, mock_input, run_program):
    entradas = ['6', '3', '7', '8', '3', '4', '7', '5', '345', '7', '865', '-10']
    lista_esperada = ['-10', '865', '7', '345', '5', '7', '4', '3', '8', '7', '3', '6']
    mock_input(entradas)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.split('\n')
    stdout.remove('')
    assert stdout == lista_esperada, f'Seu programa não imprimiu o esperado: {lista_esperada}, ao invés disso imprimiu: {stdout}.'


@pytest.mark.timeout(5)
def test_somente_com_zero(capsys, mock_input, run_program):
    entradas = ['0']
    lista_esperada = ['0']
    mock_input(entradas)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.split('\n')
    stdout.remove('')
    assert stdout == lista_esperada, f'Seu programa não imprimiu o esperado: {lista_esperada}, ao invés disso imprimiu: {stdout}.'


@pytest.mark.timeout(5)
def test_somente_com_negativo(capsys, mock_input, run_program):
    entradas = ['-134']
    lista_esperada = ['-134']
    mock_input(entradas)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.split('\n')
    stdout.remove('')
    assert stdout == lista_esperada, f'Seu programa não imprimiu o esperado: {lista_esperada}, ao invés disso imprimiu: {stdout}.'
