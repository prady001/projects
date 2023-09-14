import pytest
from pathlib import Path
import random


PWD = Path(__file__).parent
program = PWD / 'solution.py'

gabarito = [
    {
        "seed":2,
        "tentativas":["-1", "10", "30", "5", "3", "100", "1", "0", "2"],
        "muito_alto": 3,
        "muito_baixo": 1,
        "numero_tentativas": 5
    },
    {
        "seed":5,
        "tentativas": ["0", "10", "-100", "15", "42", "20"],
        "muito_alto": 0,
        "muito_baixo": 2,
        "numero_tentativas": 3
    },
    {
        "seed":42,
        "tentativas": ["20", "21", "5", "2", "3", "23", "4"],
        "muito_alto": 2,
        "muito_baixo": 2,
        "numero_tentativas": 5
    },
    {
        "seed":1,
        "tentativas": ["-20", "10", "100", "5"],
        "muito_alto": 1,
        "muito_baixo": 0,
        "numero_tentativas": 2
    }
]


@pytest.mark.timeout(5)
@pytest.mark.parametrize(
    'seed, chute',
    [
        pytest.param(seed, chute, id=f"chute = {chute}, sorteio = {chute}") for seed, chute in [(2, "2"), (5, "20"), (17, "17"), (42, "4"), (11, "15"), (7, "11")]
    ]
)
def test_acerta_de_primeira(capsys, run_program, mock_input, seed, chute):
    random.seed(seed)
    mock_input([chute])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido.count('Muito alto') == 0, f"Não deveria ter impresso 'Muito alto'.'"
    assert obtido.count('Muito baixo') == 0, f"Não deveria ter impresso 'Muito baixo'.'"
    assert obtido.count('Acertou em 1 tentativas') == 1, f"Algo deu errado! Deveria ter impresso 'Acertou em 1 tentativas'.'"


@pytest.mark.timeout(5)
@pytest.mark.parametrize(
    'detalhes',
    [
        pytest.param(detalhes, id=f"número sorteado = {detalhes['tentativas'][-1]}") for detalhes in gabarito
    ]
)
def test_algumas_tentativas(capsys, run_program, mock_input, detalhes):
    random.seed(detalhes["seed"])
    mock_input(detalhes["tentativas"])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido.count('Muito alto') == detalhes["muito_alto"], f"Algo deu errado! Deveria ter impresso 'Muito alto' {detalhes['muito_alto']} vezes, mas foi impresso {obtido.count('Muito alto')} vezes."
    assert obtido.count('Muito baixo') == detalhes["muito_baixo"], f"Algo deu errado! Deveria ter impresso 'Muito baixo' {detalhes['muito_baixo']} vezes, mas foi impresso {obtido.count('Muito baixo')} vezes."
    assert obtido.count(f'Acertou em {detalhes["numero_tentativas"]} tentativas') == 1, f"Algo deu errado! Deveria ter impresso 'Acertou em {detalhes['numero_tentativas']} tentativas'.'"
