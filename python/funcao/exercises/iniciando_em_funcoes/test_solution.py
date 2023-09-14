from pathlib import Path
import pytest
import inspect
import math

from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import graus_para_radianos
except:
    pass
    

PWD = Path(__file__).parent
program = PWD / 'solution.py'


def test_mostrou_cosseno_de_30_e_120(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    linhas = stdout.strip().split('\n')
    assert linhas[0].startswith('0.866'), f'A primeira linha não mostra o cosseno de 30 graus. Foi mostrado {linhas[0]}, mas era esperado aproximadamente 0.866'
    assert linhas[1].startswith('-0.499'), f'A segunda linha não mostra o cosseno de 120 graus. Foi mostrado {linhas[1]}, mas era esperado aproximadamente -0.499'


def test_definiu_funcao_graus_para_radianos():
    util.function_exists_in_module(solution, 'graus_para_radianos')

    sig = inspect.signature(graus_para_radianos)
    assert len(sig.parameters) == 1, 'A função graus_para_radianos deverá receber exatamente um parâmetro.'


def test_graus_para_radianos_devolve_valores_corretos():
    util.function_exists_in_module(solution, 'graus_para_radianos')

    correto30 = math.radians(30)
    solucao30 = graus_para_radianos(30)
    assert correto30 == pytest.approx(solucao30, 0.001)

    correto120 = math.radians(120)
    solucao120 = graus_para_radianos(120)
    assert correto120 == pytest.approx(solucao120, 0.001)


def test_graus_para_radianos_chamada_2_vezes():
    util.function_exists_in_module(solution, 'graus_para_radianos')
    
    with open('solution.py') as f:
        prog_contents = f.read()

    loc_def = prog_contents.find('def graus_para_radianos')
    loc_post_def = prog_contents[loc_def:].find('\n') + loc_def

    assert prog_contents[loc_post_def:].count('graus_para_radianos(') == 2
