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
        try:
            complexo = complex(stdout)
        except ValueError:
            raise AssertionError('Para este exercício, imprima somente o valor calculado e nada mais.')

        raise AssertionError('Verifique se as operações matemáticas estão sendo realizadas na ordem correta.\nVeja se -5**2 produz o valor esperado.\nTalvez você precise utilizar parênteses para definir a ordem de precedência das operações.')

    assert obtido == 3, f'Algo deu errado! Era esperado 3.0, mas foi obtido {obtido}.\nVerifique se as operações matemáticas estão sendo realizadas na ordem correta.\nTalvez você precise utilizar parênteses para definir a ordem de precedência das operações.'
