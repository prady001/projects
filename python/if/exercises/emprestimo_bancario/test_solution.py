import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('valor_casa, salario, anos', [
    pytest.param(valor_casa, salario, anos, id=f'valor da casa = {valor_casa}, salario = {salario}, anos = {anos}')
    for valor_casa, salario, anos in [
        ('50000', '1500', '10'),
        ('100000', '1500', '20'),
        ('180000', '5000', '10'),
        ('200000', '5000', '20'),
        ('1000000', '50000', '10'),
    ]
])
def test_empréstimo_aprovado(valor_casa, salario, anos, run_program, capsys, mock_input):
    mock_input([valor_casa, salario, anos])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'Você não imprimiu nenhuma mensagem informando se o empréstimo foi aprovado ou não.'

    assert stdout == 'Empréstimo aprovado', f'Algo deu errado, seu programa deveria imprimir "Empréstimo aprovado", porém foi impresso "{stdout}".'


@pytest.mark.timeout(5)
@pytest.mark.parametrize('valor_casa, salario, anos', [
    pytest.param(valor_casa, salario, anos, id=f'valor da casa = {valor_casa}, salario = {salario}, anos = {anos}')
    for valor_casa, salario, anos in [
        ('50000', '0', '1'),
        ('50000', '1000', '5'),
        ('100000', '1500', '10'),
        ('200000', '5000', '5'),
        ('1000000', '50000', '5'),
    ]
])
def test_empréstimo_não_aprovado(valor_casa, salario, anos, run_program, capsys, mock_input):
    mock_input([valor_casa, salario, anos])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()
    assert len(stdout) > 0, 'Você não imprimiu nenhuma mensagem informando se o empréstimo foi aprovado ou não.'

    assert stdout == 'Empréstimo não aprovado', f'Algo deu errado, seu programa deveria imprimir "Empréstimo não aprovado", porém foi impresso "{stdout}".'
