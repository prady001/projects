import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / "solution.py"

def test_nao_estragou_codigo_inicial(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    linhas = stdout.split('\n')
    assert len(linhas) >= 5, 'Não modifique o código original!'
    assert '\n'.join(linhas[:5]) == '''Usando alguns operadores numéricos:
5
-1
6
3.0''', 'Não modifique o código original!'


def test_adicionou_exponenciacao(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    assert '8\n' in stdout, 'O resultado da exponenciação não aparece na saída do programa.'

    with open(program, encoding='utf-8') as f:
        codigo_sem_espacos = f.read().replace(' ', '')

    assert 'print(2**3)' in codigo_sem_espacos, 'O cálculo de exponenciação não foi adicionado igual ao mostrado no exercício.'


def test_adicionou_divisoes(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    resultado_divisoes = '''2.3333333333333335
2
1
'''
    assert resultado_divisoes in stdout, 'O resultado das divisões não aparece na saída do programa.'

    with open(program, encoding='utf-8') as f:
        codigo_sem_espacos = f.read().replace(' ', '')

    codigos_divisoes = ['print(7/3)', 'print(7//3)', 'print(7%3)']

    assert all(codigo in codigo_sem_espacos for codigo in codigos_divisoes), 'O cálculo das divisões não foi adicionado igual ao mostrado no exercício.'

    anterior = -1
    for codigo in codigos_divisoes:
        atual = codigo_sem_espacos.index(codigo)
        assert anterior < atual, 'O cálculo das divisões não foi adicionado na mesma ordem mostrada no exercício. Lembre-se que a ordem das operações é importante.'
        anterior = atual


def test_adicionou_parenteses(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    resultado_parenteses = '-15'
    assert resultado_parenteses in stdout, 'O resultado da conta com parênteses não aparece na saída do programa.'

    with open(program, encoding='utf-8') as f:
        codigo_sem_espacos = f.read().replace(' ', '')

    codigo_parenteses = 'print((1+2)*(-3-2))'

    assert codigo_parenteses in codigo_sem_espacos, 'O código da expressão com parênteses não foi adicionado igual ao mostrado no exercício.'


def test_conta_ultimo_exercicio(capsys, run_program):
    run_program(program)
    stdout, _ = capsys.readouterr()

    resultado_conta = '27.5'
    assert resultado_conta in stdout, 'O resultado da conta do último exercício não aparece na saída do programa.'

    with open(program, encoding='utf-8') as f:
        prog_contents = f.read().rstrip().split('\n')

    ultima_linha = prog_contents[-1]

    for operacao in '+*/':
        assert operacao in ultima_linha, 'Você deve calcular usando Python ao invés de digitar o resultado final.'
