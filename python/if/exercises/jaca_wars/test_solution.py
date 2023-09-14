import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'

v_perto = [30, 30, 40]
v_longe = [60, 40, 40]
v_acertou = [31.5, 31.5, 40]

a_perto = [45, 40, 15]
a_longe = [45, 40, 20]
a_acertou = [45, 40, 18.5]

@pytest.mark.timeout(5)
@pytest.mark.parametrize('velocidade, angulo', [
    pytest.param(velocidade, angulo, id=f'velocidade = {velocidade}, angulo = {angulo}')
    for velocidade, angulo in zip(v_perto, a_perto)
])
def test_lancamento_de_jaca_muito_perto(velocidade, angulo, capsys, mock_input, run_program):
    mock_input([str(velocidade), str(angulo)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert len(obtido) > 0, 'O programa não imprimiu nada.'

    msg = f'Algo deu errado. Era esperado que fosse impresso "Muito perto", porém foi impresso "{obtido}".'
    if obtido == 'muito perto':
        msg += 'Note que algumas letras devem ser impressas em maiúsculo.'

    assert obtido == 'Muito perto', msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('velocidade, angulo', [
    pytest.param(velocidade, angulo, id=f'velocidade = {velocidade}, angulo = {angulo}')
    for velocidade, angulo in zip(v_longe, a_longe)
])
def test_lancamento_de_jaca_muito_longe(velocidade, angulo, capsys, mock_input, run_program):
    mock_input([str(velocidade), str(angulo)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()

    assert len(obtido) > 0, 'O programa não imprimiu nada.'

    msg = f'Algo deu errado. Era esperado que fosse impresso "Muito longe", porém foi impresso "{obtido}".'
    if obtido == 'muito longe':
        msg += 'Note que algumas letras devem ser impressas em maiúsculo.'

    assert obtido == 'Muito longe', msg


@pytest.mark.timeout(5)
@pytest.mark.parametrize('velocidade, angulo', [
    pytest.param(velocidade, angulo, id=f'velocidade = {velocidade}, angulo = {angulo}')
    for velocidade, angulo in zip(v_acertou, a_acertou)
])
def test_lancamento_de_jaca_acertou(velocidade, angulo, capsys, mock_input, run_program):
    mock_input([str(velocidade), str(angulo)])
    run_program(program)
    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    assert len(obtido) > 0, 'O programa não imprimiu nada.'

    msg = f'Algo deu errado. Era esperado que fosse impresso "Acertou!", porém foi impresso "{obtido}".'
    if obtido == 'acertou!':
        msg += 'Note que algumas letras devem ser impressas em maiúsculo.'

    assert obtido == 'Acertou!', msg
