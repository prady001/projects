import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / "solution.py"

def test_expressão_numérica_construída_corretamente(capsys, run_program):
    run_program(program)

    stdout, _ = capsys.readouterr()
    assert len(stdout) > 0, 'Você não imprimiu o resultado final.\nUtilize o comando print para imprimir o valor calculado.'

    try:
        obtido = float(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o valor calculado e nada mais.')

    assert obtido == pytest.approx(2.4285714285714284), f'Algo deu errado! Era esperado 2.4285714285714284, mas foi obtido {obtido}.\nVerifique se as operações matemáticas estão sendo realizadas na ordem correta.\nTalvez você precise utilizar parênteses para definir a ordem de precedência das operações.'
