import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'

@pytest.mark.timeout(5)
@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado, id=f'valor da conta = {entrada}')
    for entrada, esperado in [
        ('1.99','Valor da conta com 10%: R$ 2.19'),
        ('9.99','Valor da conta com 10%: R$ 10.99'),
        ('100','Valor da conta com 10%: R$ 110.00'),
        ('123.45','Valor da conta com 10%: R$ 135.80'),
    ]
])
def test_valor_da_conta(entrada, esperado, run_program, capsys, mock_input):
    mock_input([entrada])
    run_program(program)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'O programa não imprimiu nada. Era esperado que fosse impresso uma mensagem com o valor da conta.'

    msg = f'Algo deu errado, para o valor da conta = {entrada} seu programa deveria imprimir:\n{esperado}\nporém imprimiu:{stdout}.'
    if esperado.lower() in stdout.lower():
        msg+= 'Verifique se o programa está imprimindo a mensagem exatamente como foi pedida pelo enunciado e nada mais.\nNote também que o valor da conta deve ser apresentado com duas casas decimais.'

    assert stdout == esperado, msg
