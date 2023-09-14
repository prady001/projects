from pathlib import Path
from unittest.mock import mock_open, patch

PWD = Path(__file__).parent
program = PWD / 'solution.py'


def test_estoque_arquivo_exemplo(capsys, run_program):
    run_program(program)

    stdout, _ = capsys.readouterr()
    expected = 94.52
    hit = float(stdout.strip())
    assert hit == expected, f'O seu print retornou o valor de R${hit}, porém o correto seria R${expected}'


def test_estoque_vazio(capsys, run_program):
    estoque = '''
{"produtos": []}
    '''
    with patch('builtins.open', mock_open(read_data=estoque)) as m:
        run_program(program)

        stdout, _ = capsys.readouterr()
        resposta_aluno = float(stdout.strip())
        assert resposta_aluno == 0, 'Resultado diferente de 0 para estoque sem produtos.'


def test_estoque_com_um_produto(capsys, run_program):
    estoque = '''
{"produtos": [
    {"produto": "p1", "quantidade": 1, "valor": 5}
]}
    '''
    with patch('builtins.open', mock_open(read_data=estoque)) as m:
        run_program(program)

        stdout, _ = capsys.readouterr()
        resposta_aluno = float(stdout.strip())
        assert resposta_aluno == 5, f'O seu print retornou o valor de R${resposta_aluno}, porém o correto seria R$5,00. Estoque é {estoque}'
