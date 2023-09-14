import pytest
from pathlib import Path
import random


PWD = Path(__file__).parent
program = PWD / 'solution.py'
gabarito = [
    (2, "10", "Muito alto"),
    (7, "20", "Muito alto"),
    (11," 1", "Muito baixo"),
    (5, "10", "Muito baixo"),
    (17," 17", "Acertou"),
    (42," 4", "Acertou")
]


@pytest.mark.timeout(5)
@pytest.mark.parametrize(
    'seed,chute,esperado',
    [
        pytest.param(seed, chute, esperado, id=f"chute = {chute}, sorteio = {esperado}") for seed, chute, esperado in gabarito
    ]
)
def test_adivinha_numero(capsys, run_program, mock_input, seed, chute, esperado):
    random.seed(seed)
    mock_input([chute])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert obtido == esperado, f'Algo deu errado! Era esperado {esperado}, mas foi obtido {obtido}.'
