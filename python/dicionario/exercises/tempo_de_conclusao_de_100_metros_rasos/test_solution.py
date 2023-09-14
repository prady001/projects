import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_tempo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_tempo')


def test_corrida_sozinho():
    entrada = {"Nico Uno": 10}
    tempos = calcula_tempo(entrada)
    assert (
        len(tempos) == 1
    ), f"Dicionário de resultados tem número de elementos diferente de 1. Saída: {tempos}"
    assert tempos["Nico Uno"] == pytest.approx(4.472, 0.1)


def test_empate_todos():
    entrada = {
        "Nico Uno": 3,
        "Horácio P. Genaro": 3,
        "Ukibe Nokome": 3,
        "Maurício Melo": 3,
        "Abigail Oliveira": 3,
    }
    tempos = calcula_tempo(entrada)
    assert (
        len(tempos) == 5
    ), f"Dicionário de resultados tem número de elementos diferente de 5. Saída: {tempos}"
    for k, v in tempos.items():
        assert v == pytest.approx(
            8.165, 0.1
        ), "Todos os atletas tem a mesma aceleração e terminam em 8.165s"


def test_primeiro_ganha():
    entrada = {
        "Nico Uno": 30,
        "Horácio P. Genaro": 15,
        "Ukibe Nokome": 3,
        "Maurício Melo": 20,
        "Abigail Oliveira": 17,
    }
    saidas = {
        "Nico Uno": pytest.approx(2.581, 0.1),
        "Horácio P. Genaro": pytest.approx(3.651, 0.1),
        "Ukibe Nokome": pytest.approx(8.165, 0.1),
        "Maurício Melo": pytest.approx(3.162, 0.1),
        "Abigail Oliveira": pytest.approx(3.430, 0.1),
    }

    tempos = calcula_tempo(entrada)
    assert (
        len(tempos) == 5
    ), f"Dicionário de resultados tem número de elementos diferente de 5. Saída: {tempos}"
    for k in saidas:
        assert (
            tempos[k] == saidas[k]
        ), f"O tempo de {k} foi diferente de {saidas[k]}. Recebido: {tempos[k]}"


def test_ultimo_ganha():
    entrada = {
        "Nico Uno": 10,
        "Horácio P. Genaro": 15,
        "Ukibe Nokome": 3,
        "Maurício Melo": 20,
        "Abigail Oliveira": 30,
    }
    saidas = {
        "Nico Uno": pytest.approx(4.472, 0.1),
        "Horácio P. Genaro": pytest.approx(3.651, 0.1),
        "Ukibe Nokome": pytest.approx(8.165, 0.1),
        "Maurício Melo": pytest.approx(3.162, 0.1),
        "Abigail Oliveira": pytest.approx(2.581, 0.1),
    }

    tempos = calcula_tempo(entrada)
    assert (
        len(tempos) == 5
    ), f"Dicionário de resultados tem número de elementos diferente de 5. Saída: {tempos}"
    for k in saidas:
        assert (
            tempos[k] == saidas[k]
        ), f"O tempo de {k} foi diferente de {saidas[k]}. Recebido: {tempos[k]}"
