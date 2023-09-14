import pytest
from pathlib import Path
import inspect
import funcoes


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.parametrize('salario, esperado',
    [
        pytest.param(salario, esperado, id=f'salario = {salario}')
            for salario, esperado in [
                (1000, 75.0),
                (1045, 78.375),
                (2000, 180.0),
                (2089.6, 188.064),
                (3000, 360.0),
                (3134.4, 376.128),
                (4000, 560.0),
                (6101.06, 854.1484000000002),
                (7000, 671.12)
            ]
])
def test_contribuição_para_o_inss(salario, esperado):
    all_functions = inspect.getmembers(funcoes, inspect.isfunction)
    assert any([f[0] == 'calcula_contribuicao_inss' for f in all_functions]), 'A função calcula_contribuicao_inss não foi definida!'

    obtido = funcoes.calcula_contribuicao_inss(salario)
    assert obtido == pytest.approx(esperado), f'Algo deu errado para o salario {salario}.\nEra esperado {esperado} mas foi obtido {obtido}.'


@pytest.mark.parametrize('salario, dependentes, esperado',
    [
        pytest.param(salario, dependentes, esperado, id=f'salario = {salario}, dependentes = {dependentes}')
            for salario, dependentes, esperado in [
                (1000, 1, 735.41),
                (1045, 2, 587.4449999999999),
                (2000, 0, 1820.0),
                (2089.6, 1, 1711.946),
                (3000, 2, 2260.82),
                (3134.4, 3, 2189.502),
                (4000, 0, 3440.0),
                (6101.06, 1, 5057.3216),
                (7000, 2, 5949.7)
            ]
])
def test_base_de_cálculo(salario, dependentes, esperado):
    all_functions = inspect.getmembers(funcoes, inspect.isfunction)
    assert any([f[0] == 'calcula_base_de_calculo' for f in all_functions]), 'A função calcula_base_de_calculo não foi definida!'

    obtido = funcoes.calcula_base_de_calculo(salario, dependentes)
    assert obtido == pytest.approx(esperado), f'Algo deu errado para o salario {salario} e {dependentes} dependente(s).\nEra esperado {esperado} mas foi obtido {obtido}.'

@pytest.mark.parametrize('salario, dependentes, esperado',
    [
        pytest.param(salario, dependentes, esperado, id=f'salario = {salario}, dependentes = {dependentes}')
            for salario, dependentes, esperado in [
                (1000, 1, 0),
                (1045, 2, 0),
                (2000, 0, 0),
                (2089.6, 1, 0),
                (3000, 2, 26.761499999999984),
                (3134.4, 3, 21.412649999999985),
                (4000, 0, 161.2),
                (6101.06, 1, 521.4034400000002),
                (7000, 2, 766.8075)
            ]
])
def test_irrf_simplificado(salario, dependentes, esperado):
    all_functions = inspect.getmembers(funcoes, inspect.isfunction)
    assert any([f[0] == 'calcula_irrf' for f in all_functions]), 'A função calcula_irrf não foi definida!'

    obtido = funcoes.calcula_irrf(salario, dependentes)
    assert obtido == pytest.approx(esperado), f'Algo deu errado para o salario {salario} e {dependentes} dependente(s).\nEra esperado {esperado} mas foi obtido {obtido}.'


@pytest.mark.parametrize('salario, dependentes, esperado',
    [
        pytest.param(salario, dependentes, esperado, id=f'salario = {salario}; dependentes = {dependentes}')
            for salario, dependentes, esperado in [
                ("1045.00", "1", 0.00),
                ("1903.98", "1", 0.00),
                ("2089.60", "2", 0.00),
                ("3000.00", "0", 55.20),
                ("3134.40", "0", 64.07),
                ("3134.41", "1", 45.15),
                ("6101.06", "2", 469.27),
                ("6101.07", "4", 415.33)
    ]
])
@pytest.mark.timeout(5)
def test_versão_final_do_irrf_simplificado(salario, dependentes, esperado, run_program, capsys, mock_input):
    with open(program, encoding='utf-8') as file:
        content = file.read()

    assert len(content) > 0, "O programa pedido no exercício ainda não foi implementado!"

    mock_input([salario, dependentes])
    run_program(program)

    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Você não imprimiu o valor do IRRF.'

    try:
        obtido = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor do IRRF e nada mais.')
    assert obtido == esperado, f'Algo deu errado. Para o salário {salario} e {dependentes} dependente(s).\n Seu programa deveria imprimir {esperado}, porém, imprimiu {obtido}.'
