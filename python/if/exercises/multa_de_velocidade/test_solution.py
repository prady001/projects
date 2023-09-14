import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


def test_de_velocidade_nula(capsys, mock_input, run_program):
    velocidade = '0'
    multa = 'Não foi multado'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_21(capsys, mock_input, run_program):
    velocidade = '21'
    multa = 'Não foi multado'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_45(capsys, mock_input, run_program):
    velocidade = '45'
    multa = 'Não foi multado'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_66(capsys, mock_input, run_program):
    velocidade = '66'
    multa = 'Não foi multado'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_de_corte_80(capsys, mock_input, run_program):
    velocidade = '80'
    multa = 'Não foi multado'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_88(capsys, mock_input, run_program):
    velocidade = '88'
    multa = '40.00'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
        if stdout == multa[0:3] and multa != 'Não foi multado':
            dica = f'\nProvavelmente, você só está imprimindo sem as 2 casas decimais requisitadas no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_99(capsys, mock_input, run_program):
    velocidade = '99'
    multa = '95.00'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
        if stdout == multa[0:3] and multa != 'Não foi multado':
            dica = f'\nProvavelmente, você só está imprimindo sem as 2 casas decimais requisitadas no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_100(capsys, mock_input, run_program):
    velocidade = '100' 
    multa = '100.00'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
        if stdout == multa[0:3] and multa != 'Não foi multado':
            dica = f'\nProvavelmente, você só está imprimindo sem as 2 casas decimais requisitadas no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'


def test_de_velocidade_378(capsys, mock_input, run_program):
    velocidade = '378'
    multa = '1490.00'
    mock_input([velocidade])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    dica = ''
    if stdout != multa:
        dica = f'\nSeu programa imprimiu o seguinte valor {stdout}, que é diferente do esperado {multa}. Confira se você está seguindo os critérios definidos no enunciado.'
        if stdout == multa[0:3] and multa != 'Não foi multado':
            dica = f'\nProvavelmente, você só está imprimindo sem as 2 casas decimais requisitadas no enunciado.'
    assert stdout == multa, f'Algo deu errado na hora de imprimir a multa (ou não) do carro.{dica}'
