import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.parametrize('idade', [16, 17, 49, 80])
def test_idade_maior_que_16_pode_votar(capsys, mock_input, run_program, idade):
    mock_input([str(idade)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert obtido == 'Pode votar!', f'Algo deu errado. Era esperado que fosse impresso "Pode votar!", porém foi impresso "{obtido}".'

@pytest.mark.parametrize('idade', [2, 5, 15, 10])
def test_idade_menor_que_16_não_pode_votar(capsys, mock_input, run_program, idade):
    mock_input([str(idade)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido == 'Espere um pouco!', f'Algo deu errado. Era esperado que fosse impresso "Espere um pouco!", porém foi impresso "{obtido}".'
