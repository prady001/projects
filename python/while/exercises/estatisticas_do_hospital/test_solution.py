import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'

@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado, id=f'idades digitadas = {entrada}')
    for entrada, esperado in [
        (['100', '-1'], ['0.00', '0.00', '0.00', '0.00', '0.00', '100.00']),
        (['0', '64', '-3'], ['50.00', '0.00', '0.00', '0.00', '0.00', '50.00']),
        (['11', '12', '17', '18', '-6'], ['25.00', '50.00', '25.00', '0.00', '0.00', '0.00']),
        (['30', '10', '20', '35', '50', '55', '90', '70', '100', '-1'], ['11.11', '0.00', '11.11', '22.22', '22.22', '33.33'])
    ]
])
def test_estatísticas_do_hospital(entrada, esperado, run_program, capsys, mock_input):
    mock_input(entrada)
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    obtido = stdout
    string_esperado = f'''0-11 anos: {esperado[0]} %
12-17 anos: {esperado[1]} %
18-25 anos: {esperado[2]} %
26-35 anos: {esperado[3]} %
36-59 anos: {esperado[4]} %
Acima de 60 anos: {esperado[5]} %'''

    assert len(stdout) > 0, 'O programa não imprimiu nada no terminal.'
    assert obtido.replace(' ', '').replace('\n', '') == string_esperado.replace(' ', '').replace('\n', ''), f'Algo deu errado, seu programa deveria imprimir:\n{string_esperado}, porém imprimiu:\n{obtido}'
