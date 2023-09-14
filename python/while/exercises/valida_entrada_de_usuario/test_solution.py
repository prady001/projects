import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'
entradas = [
    ["2"],
    ["15","2"],
    ["31", "5", "9", "0"],
    ["111", "93", "431", "1000"],
    ["1", "3", "5", "7", "9", "42"],
]


@pytest.mark.timeout(5)
@pytest.mark.parametrize(
    'entrada',
    [
        pytest.param(entrada, id=f"entrada = {entrada}") for entrada in entradas
    ]
)
def test_algumas_entradas(capsys, run_program, mock_input, entrada):
    mock_input(entrada)
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido.count('Este número não é par, tente novamente.') == len(entrada)-1, f"Algo deu errado! Deveria ter impresso 'Este número não é par, tente novamente.' {len(entrada)-1} vezes, mas foi impresso {obtido.count('Este número não é par, tente novamente.')} vezes."
    assert obtido.count(f'Você digitou: {entrada[-1]}') == 1, f"Algo deu errado! Era esperado que fosse impresso 'Você digitou: {entrada[-1]}'"
