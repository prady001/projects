import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'

@pytest.mark.timeout(5)
@pytest.mark.parametrize('respostas', [
    pytest.param(respostas, id=f'respostas = {respostas}')
    for respostas in [
        (['não', 'não', 'não', 'não', 'não']),
        (['sim', 'não', 'não', 'não', 'não']),
        (['não', 'sim', 'não', 'não', 'não']),
        (['não', 'não', 'sim', 'não', 'não']),
        (['não', 'não', 'não', 'sim', 'não']),
        (['não', 'não', 'não', 'não', 'sim']),
    ]
])
def test_classificação_inocente(respostas, run_program, capsys, mock_input):
    mock_input(respostas)
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nada no terminal.'
    if stdout == 'inocente':
        msg += ' Note que o exercício espera que a primeira letra da palavra impressa seja maiúscula.'
    msg = f'Algo deu errado, para as respostas {respostas}, era esperado que o programa imprimisse "Inocente" e porém imprimiu {stdout}.'
    assert stdout == 'Inocente', msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('respostas', [
    pytest.param(respostas, id=f'respostas = {respostas}')
    for respostas in [
        (['sim', 'sim', 'não', 'não', 'não']),
        (['sim', 'não', 'sim', 'não', 'não']),
        (['sim', 'não', 'não', 'sim', 'não']),
        (['sim', 'não', 'não', 'não', 'sim']),
        (['não', 'sim', 'sim', 'não', 'não']),
        (['não', 'sim', 'não', 'sim', 'não']),
        (['não', 'sim', 'não', 'não', 'sim']),
        (['não', 'não', 'sim', 'sim', 'não']),
        (['não', 'não', 'sim', 'não', 'sim']),
        (['não', 'não', 'não', 'sim', 'sim']),
    ]
])
def test_classificação_padawan(respostas, run_program, capsys, mock_input):
    mock_input(respostas)
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nada no terminal.'
    if stdout == 'padawan':
        msg += ' Note que o exercício espera que a primeira letra da palavra impressa seja maiúscula.'
    msg = f'Algo deu errado, para as respostas {respostas}, era esperado que o programa imprimisse "Padawan" e porém imprimiu {stdout}.'
    assert stdout == 'Padawan', msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('respostas', [
    pytest.param(respostas, id=f'respostas = {respostas}')
    for respostas in [
        (['sim', 'sim', 'sim', 'não', 'não']),
        (['sim', 'sim', 'não', 'sim', 'não']),
        (['sim', 'sim', 'não', 'não', 'sim']),
        (['sim', 'não', 'sim', 'sim', 'não']),
        (['sim', 'não', 'sim', 'não', 'sim']),
        (['sim', 'não', 'não', 'sim', 'sim']),
        (['não', 'sim', 'sim', 'sim', 'não']),
        (['não', 'sim', 'sim', 'não', 'sim']),
        (['não', 'sim', 'não', 'sim', 'sim']),
        (['não', 'não', 'sim', 'sim', 'sim']),
        (['sim', 'sim', 'sim', 'sim', 'não']),
        (['sim', 'sim', 'sim', 'não', 'sim']),
        (['sim', 'sim', 'não', 'sim', 'sim']),
        (['sim', 'não', 'sim', 'sim', 'sim']),
        (['não', 'sim', 'sim', 'sim', 'sim']),
    ]
])
def test_classificação_jedi(respostas, run_program, capsys, mock_input):
    mock_input(respostas)
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nada no terminal.'
    if stdout == 'jedi':
        msg += ' Note que o exercício espera que a primeira letra da palavra impressa seja maiúscula.'
    msg = f'Algo deu errado, para as respostas {respostas}, era esperado que o programa imprimisse "Jedi" e porém imprimiu {stdout}.'
    assert stdout == 'Jedi', msg


@pytest.mark.timeout(5)
def test_classificação_one_with_the_force(run_program, capsys, mock_input):
    respostas = ['sim', 'sim', 'sim', 'sim', 'sim']
    mock_input(respostas)
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu nada no terminal.'
    if stdout == 'one with the force':
        msg += ' Note que o exercício espera que a primeira letra da palavra impressa seja maiúscula.'
    msg = f'Algo deu errado, para as respostas {respostas}, era esperado que o programa imprimisse "One with the Force" e porém imprimiu {stdout}.'
    assert stdout == 'One with the Force', msg
