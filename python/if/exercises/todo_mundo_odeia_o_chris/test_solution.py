import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.parametrize('nome', ['thiago', 'andrew', 'barbara', 'Thiago', 'Andrew', 'Barbara'])
def test_nomes_diferentes_de_chris(capsys, mock_input, run_program, nome):
    mock_input([nome])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    esperado = f'Olá, {nome}'

    msg = ''
    if obtido == esperado.lower():
        msg = 'Texto correto porém está em minúsculo. Verifique o print.'
        raise AssertionError(msg)

    elif obtido == esperado:
        if obtido.count(esperado) == 1 and obtido.count('Todo mundo odeia o Chris') == 0:
            assert True
        else:
            msg = f'Resposta muito próxima da esperada. Verifique os espaços entre as palavras.'
            raise AssertionError(msg)
    else:
        msg = f'Era esperado "{esperado}". e foi obtido "{obtido}".'
        raise AssertionError(msg)


def test_com_input_chris(capsys, mock_input, run_program):
    mock_input(['Chris'])
    run_program(program)

    stdout, _ = capsys.readouterr()
    obtido = stdout.strip()
    esperado = 'Todo mundo odeia o Chris'
    
    msg = ''
    if obtido == esperado.lower():
        msg = 'Texto correto porém está em minúsculo. Verifique o print.'
        raise AssertionError(msg)

    elif obtido == esperado:
        if obtido.count(esperado) == 1 and obtido.count('Olá, Chris') == 0:
            assert True
        else:
            msg = f'Resposta muito próxima da esperada. Verifique os espaços entre as palavras.'
            raise AssertionError(msg)
    else:
        msg = f'Era esperado "{esperado}". e foi obtido "{obtido}".'
        raise AssertionError(msg)
