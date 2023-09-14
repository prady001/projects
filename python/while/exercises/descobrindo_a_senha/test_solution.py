import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_senhas_de_exemplo(capsys, mock_input, run_program):
    inputs = ['senha', 'senha1', 'seila', 'desisto']
    mock_input(inputs)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Você acertou a senha!', f'Algo deu errado! Ao acertar a senha era esperado que fosse impresso a mensagem "Você acertou a senha!", porém foi impresso "{stdout}".'


@pytest.mark.timeout(5)
def test_muitas_senhas_erradas(capsys, mock_input, run_program):
    inputs = ['senha', 'senha1', 'senha1', 'senha1', 'senha1', 'senha1', 'senha1', 'senha1', 'senha1', 'senha1', 'seila', 'desisto']
    mock_input(inputs)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Você acertou a senha!', f'Algo deu errado! Ao acertar a senha era esperado que fosse impresso a mensagem "Você acertou a senha!", porém foi impresso "{stdout}".'


@pytest.mark.timeout(5)
def test_somente_senha_correta(capsys, mock_input, run_program):
    inputs = ['desisto']
    mock_input(inputs)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Você acertou a senha!', f'Algo deu errado! Ao acertar a senha era esperado que fosse impresso a mensagem "Você acertou a senha!", porém foi impresso "{stdout}".'
