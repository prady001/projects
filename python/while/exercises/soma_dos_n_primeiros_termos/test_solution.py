import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'
GABARITO = {0: 0, 1: 1.0, 2: 1.5, 3: 1.75, 4: 1.875, 5: 1.9375, 6: 1.96875, 7: 1.984375, 8: 1.9921875, 9: 1.99609375, 10: 1.998046875, 11: 1.9990234375, 12: 1.99951171875, 13: 1.999755859375, 14: 1.9998779296875, 15: 1.99993896484375, 16: 1.999969482421875, 17: 1.9999847412109375, 18: 1.9999923706054688, 19: 1.9999961853027344, 20: 1.9999980926513672, 21: 1.9999990463256836, 22: 1.9999995231628418, 23: 1.999999761581421, 24: 1.9999998807907104, 25: 1.9999999403953552}


@pytest.mark.parametrize(
    'n',
    [
        pytest.param(n, id=f'n={n}') for n in list(GABARITO.keys()) + [50, 75, 100]
    ]
)
@pytest.mark.timeout(5)
def test_soma_dos_n_primeiros_termos(capsys, mock_input, run_program, n):
    entrada = str(n)
    mock_input([entrada])
    run_program(program)

    stdout, _ = capsys.readouterr()
    esperado = GABARITO.get(n, 2.0)

    assert len(stdout) > 0, 'O programa não imprimiu a soma.'

    try:
        obtido = float(stdout.strip())
    except ValueError:
        raise AssertionError(f'Algo de errado aconteceu, era esperado {esperado}.\n Mas seu programa imprimiu "{stdout.strip()}". Imprima somente o número.')

    assert obtido == pytest.approx(esperado), f'Algo de errado aconteceu, era esperado {esperado}.\n Mas foi obtido: {obtido}'
