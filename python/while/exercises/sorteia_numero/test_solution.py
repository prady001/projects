import pytest
from pathlib import Path
import random


PWD = Path(__file__).parent
program = PWD / 'solution.py'
gabarito_sorteando_alguns_numeros = [
    (2, 2),
    (5, 20),
    (17, 17),
    (42, 4),
    (11, 15),
    (7, 11)
]


@pytest.mark.parametrize(
    'seed,esperado',
    [
        pytest.param(seed, esperado, id=f"esperado = {esperado}") for seed, esperado in gabarito_sorteando_alguns_numeros
    ]
)
def test_sorteando_alguns_numeros(capsys, run_program, seed, esperado):
    random.seed(seed)
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'O programa não imprimiu o número sorteado.'

    try:
        obtido = int(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o número sorteado e nada mais.')
    mensagem = ""

    if obtido > 20 or obtido <=0:
        mensagem = "\nNúmero sorteado deveria ser um número entre 1 a 20."

    assert obtido == esperado, f'Algo deu errado! Era esperado {esperado}, mas foi obtido {obtido}.{mensagem}'
