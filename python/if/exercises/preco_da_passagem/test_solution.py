import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'

gabarito = {150: '75.00', 160: '80.00', 170: '85.00', 180: '90.00', 190: '95.00', 200: '100.00', 210: '104.50', 220: '109.00', 230: '113.50', 240: '118.00', 250: '122.50', 175: '87.50', 181: '90.50', 186: '93.00', 192: '96.00', 197: '98.50', 203: '101.35', 208: '103.60', 214: '106.30',
            219: '108.55'}


@pytest.mark.parametrize(
    'distancia, esperado',
    [
        pytest.param(distancia, preco, id=f'distancia={distancia}, preco={preco}') for distancia, preco in gabarito.items()
    ]
)
def test_preco_da_passagem(capsys, mock_input, run_program, distancia, esperado):
    distancia = str(distancia)
    mock_input([distancia])
    run_program(program)

    stdout, _ = capsys.readouterr()  # saida do programa (preco)
    obtido = stdout.strip()
    assert obtido == esperado, f'Algo de errado aconteceu, era esperado {esperado}.\n Mas foi obtido:{stdout}'
