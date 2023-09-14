import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import valida_data
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'valida_data')


@pytest.mark.parametrize(
    'dia,mes,ano',
    [
        pytest.param(dia, mes, ano, id=f'dia = {dia}, mes = {mes}, ano = {ano}')
        for dia, mes, ano in [
            (31, 4, 2020),
            (31, 6, 2023),
            (31, 9, 2021),
            (31, 11, 2022),
        ]
    ]
)
def test_meses_com_30_dias(dia, mes, ano):
    obtido = valida_data(dia, mes, ano)
    assert obtido == False, f'O resultado obtido foi diferente do esperado. A data não é válida (lembre-se que alguns meses possuem apenas 30 dias!). A chamada de função valida_data({dia}, {mes}, {ano}) deveria devolver False.'


@pytest.mark.parametrize(
    'dia,mes,ano',
    [
        pytest.param(dia, mes, ano, id=f'dia = {dia}, mes = {mes}, ano = {ano}')
        for dia, mes, ano in [
            (31, 1, 2019),
            (31, 3, 2020),
            (31, 5, 2020),
            (31, 7, 2021),
            (31, 8, 2021),
            (31, 10, 2022),
            (31, 12, 2022),
        ]
    ]
)
def test_meses_com_31_dias(dia, mes, ano):
    obtido = valida_data(dia, mes, ano)
    assert obtido == True, f'O resultado obtido foi diferente do esperado. A data é válida. A chamada de função valida_data({dia}, {mes}, {ano}) deveria devolver True.'


@pytest.mark.parametrize(
    'dia,mes,ano',
    [
        pytest.param(dia, mes, ano, id=f'dia = {dia}, mes = {mes}, ano = {ano}')
        for dia, mes, ano in [
            (29, 2, 2020),
            (29, 2, 1600),
            (29, 2, 2024),
            (29, 2, 2028),
        ]
    ]
)
def test_fevereiro_em_ano_bissexto(dia, mes, ano):
    obtido = valida_data(dia, mes, ano)
    assert obtido == True, f'O resultado obtido foi diferente do esperado. A data {dia}/02/{ano} é válida, pois o ano de {ano} é bissexto. A chamada de função valida_data({dia}, {mes}, {ano}) deveria devolver True.'


@pytest.mark.parametrize(
    'dia,mes,ano',
    [
        pytest.param(dia, mes, ano, id=f'dia = {dia}, mes = {mes}, ano = {ano}')
        for dia, mes, ano in [
            (29, 2, 2019),
            (29, 2, 1700),
            (29, 2, 1900),
        ]
    ]
)
def test_fevereiro_em_ano_não_bissexto(dia, mes, ano):
    obtido = valida_data(dia, mes, ano)
    assert obtido == False, f'O resultado obtido foi diferente do esperado. A data {dia}/02/{ano} não é válida, pois o ano de {ano} não é bissexto. A chamada de função valida_data({dia}, {mes}, {ano}) deveria devolver False.'


@pytest.mark.parametrize(
    'dia,mes,ano',
    [
        pytest.param(dia, mes, ano, id=f'dia = {dia}, mes = {mes}, ano = {ano}')
        for dia, mes, ano in [
            (40, 8, 2020),
            (2, 80, 2020),
            (32, 13, 2022),
        ]
    ]
)
def test_datas_inválidas(dia, mes, ano):
    obtido = valida_data(dia, mes, ano)
    assert obtido == False, f'O resultado obtido foi diferente do esperado. A data não é válida. A chamada de função valida_data({dia}, {mes}, {ano}) deveria devolver False.'
