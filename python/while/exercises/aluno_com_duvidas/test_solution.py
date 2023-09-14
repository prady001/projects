import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_algumas_vezes(capsys, mock_input, run_program):
    mock_input(['sim', 'talvez', 'ainda um pouco',
               'não', 'já deveria ter terminado'])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido.count('Pratique mais') == 3, f'Algo deu errado! Era esperado que fosse impresso a mensagem "Pratique mais" 3 vezes, mas foi impresso { obtido.count("Pratique mais") } vezes. '
    assert obtido.count('Até a próxima') == 1, f'Algo deu errado! Era esperado que fosse impresso a mensagem "Até a próxima" uma vez, mas foi impresso { obtido.count("Até a próxima") } vezes. '


@pytest.mark.timeout(5)
def test_de_primeira(capsys, mock_input, run_program):
    mock_input(['não', 'já deveria ter terminado'])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert obtido.count('Pratique mais') == 0, f'Algo deu errado! Não era esperado que a mensagem "Pratique mais" fosse impressa.'
    assert obtido.count('Até a próxima') == 1, f'Algo deu errado! Era esperado que fosse impresso a mensagem "Até a próxima" uma vez, mas foi impresso {obtido.count("Até a próxima")} vezes. '
