import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
@pytest.mark.parametrize(
    'entrada',
    [
        pytest.param(entrada) for entrada in ["sim", "talvez", "não sei", "SIM"]
    ]
)
def test_aluno_tem_duvidas(capsys, run_program, mock_input, entrada):
    mock_input([entrada])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido == "Pratique mais", f'Algo deu errado! Era esperado "Pratique mais", mas foi obtido {obtido}.'


@pytest.mark.timeout(5)
def test_aluno_nao_tem_duvidas(capsys, run_program, mock_input):
    mock_input(["não"])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido == "Até a próxima", f'Algo deu errado! Era esperado "Até a próxima", mas foi obtido {obtido}.'
