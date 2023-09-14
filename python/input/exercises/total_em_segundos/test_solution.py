import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.parametrize('dias, horas, minutos, segundos, esperado', [
    pytest.param(dias, horas, minutos, segundos, esperado, 
            id=f'dias = {dias}; horas = {horas}, minutos = {minutos}, segundos = {segundos}, esperado = {esperado}')
    for dias, horas, minutos, segundos, esperado in [
        (2, 3, 40, 50, 186050),
        (3, 15, 25, 1, 314701),
        (10, 5, 10, 5, 882605),
        (0, 0, 0, 1, 1),
        (70, 23, 59, 59, 6134399),
        (0, 10, 10, 10, 36610),
        (0, 0, 10, 10, 610),
        (0, 0, 0, 10, 10),
        (0, 0, 0, 0, 0)
    ]
])
def test_total_segundos(dias, horas, minutos, segundos, esperado, run_program, capsys, mock_input):
    mock_input([str(dias), str(horas), str(minutos), str(segundos)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'Você não imprimiu o total em segundos.'
    try:
        output = int(stdout)
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente o total em segundos e nada mais.')
    assert output == esperado, f'Algo deu errado, seu programa deveria devolver {esperado} segundos, e devolveu {output} segundos'
