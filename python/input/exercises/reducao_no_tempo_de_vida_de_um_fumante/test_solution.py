import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / "solution.py"

lista_cigarros = [1, 4, 6, 7, 10, 15, 20]
lista_anos = [1, 2, 3, 4, 5, 6, 7]
resposta_esperada = [
    2.5347222222222223,
    20.27777777777778,
    45.625,
    70.97222222222223,
    126.73611111111111,
    228.125,
    354.8611111111111,
]


@pytest.mark.parametrize(
    "cigarros, anos, resposta",
    [
        pytest.param(
            cigarros,
            anos,
            resposta,
            id=f"Cigarros por dia = {cigarros} \n Anos fumando = {anos}",
        )
        for cigarros, anos, resposta in zip(
            lista_cigarros, lista_anos, resposta_esperada
        )
    ],
)
@pytest.mark.timeout(1)
def test_valores_corretos(capsys, mock_input, run_program, cigarros, anos, resposta):
    mock_input([str(cigarros), str(anos)])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    try:
        resposta_usuario = float(obtido)
    except ValueError:
        raise AssertionError("Imprima somente o número e nada mais")

    assert resposta_usuario == pytest.approx(
        resposta
    ), f"Resultado obtido: {obtido}. Esperado {resposta}"
