import pytest
import math
from pathlib import Path

PWD = Path(__file__).parent
program = PWD / "solution.py"


def test_penultimo_atleta_ganha(capsys, mock_input, run_program):
    mock = [
        "Nico Uno",
        "10",
        "Horácio P. Genaro",
        "15",
        "Ukibe Nokome",
        "3",
        "Maurício Melo",
        "20",
        "Abigail Oliveira",
        "17",
        "sair",
    ]
    expectedName = "Maurício Melo"
    expectedTime = math.sqrt(200 / 20)
    mock_input(mock)
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert (
        obtido.count(
            f"O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s"
        )
        == 1
    ), f"Era esperado um print com a mensagem 'O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s' mas foi obtido a mensagem '{obtido}'."


def test_apenas_um_atleta(capsys, mock_input, run_program):
    mock = ["Nico Uno", "10", "sair"]
    expectedName = "Nico Uno"
    expectedTime = math.sqrt(200 / 10)
    mock_input(mock)
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert (
        obtido.count(
            f"O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s"
        )
        == 1
    ), f"Era esperado um print com a mensagem 'O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s' mas foi obtido a mensagem '{obtido}'."


def test_inputs_apos_digitar_sair(capsys, mock_input, run_program):
    mock = [
        "Nico Uno",
        "10",
        "Horácio P. Genaro",
        "15",
        "Ukibe Nokome",
        "3",
        "sair",
        "Maurício Melo",
        "20",
        "Abigail Oliveira",
        "17",
    ]
    expectedName = "Horácio P. Genaro"
    expectedTime = math.sqrt(200 / 15)
    mock_input(mock)
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert (
        obtido.count(
            f"O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s"
        )
        == 1
    ), f"Era esperado um print com a mensagem 'O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s' mas foi obtido a mensagem '{obtido}'."


def test_primeiro_atleta_ganha(capsys, mock_input, run_program):
    mock = [
        "Nico Uno",
        "30",
        "Horácio P. Genaro",
        "15",
        "Ukibe Nokome",
        "3",
        "Maurício Melo",
        "20",
        "Abigail Oliveira",
        "17",
        "sair",
    ]
    expectedName = "Nico Uno"
    expectedTime = math.sqrt(200 / 30)
    mock_input(mock)
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert (
        obtido.count(
            f"O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s"
        )
        == 1
    ), f"Era esperado um print com a mensagem 'O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s' mas foi obtido a mensagem '{obtido}'."


def test_ultimo_atleta_ganha(capsys, mock_input, run_program):
    mock = [
        "Nico Uno",
        "10",
        "Horácio P. Genaro",
        "15",
        "Ukibe Nokome",
        "3",
        "Maurício Melo",
        "20",
        "Abigail Oliveira",
        "30",
        "sair",
    ]
    expectedName = "Abigail Oliveira"
    expectedTime = math.sqrt(200 / 30)
    mock_input(mock)
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert (
        obtido.count(
            f"O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s"
        )
        == 1
    ), f"Era esperado um print com a mensagem 'O vencedor é {expectedName} com tempo de conclusão de {expectedTime:.2f} s' mas foi obtido a mensagem '{obtido}'."
