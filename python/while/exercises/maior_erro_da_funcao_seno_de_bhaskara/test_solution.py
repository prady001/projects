import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'

@pytest.mark.timeout(5)
def test_ponto_de_maior_erro_da_função_de_Bhaskara(run_program, capsys):
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'O programa não imprimiu o ponto de maior erro da função de Bhāskara.'
    try:
        output = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o ponto de maior erro da função de Bhāskara e nada mais.')

    msg = f'Não chegou no resultado esperado. É esperado o valor "12", porém foi obtdo "{output}".\nDica: Olhe a documentação do math.sin e veja se você está passando o argumento da forma correta.'
    if not output.is_integer():
        msg += 'Note que o exercício pede para imprimir o ponto de maior erro. Ou seja, o programa deve imprimir o valor do número em graus.\nVeja se seu programa não está imprimindo a diferença.'

    assert output == 12, msg
