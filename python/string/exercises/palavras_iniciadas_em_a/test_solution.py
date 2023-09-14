import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


@pytest.mark.timeout(5)
def test_com_muitas_palavras(capsys, mock_input, run_program):
    palavras = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua tincidunt dui ut ornare lectus sit amet est placerat eget nunc lobortis mattis aliquam faucibus purus in massa est ultricies integer quis auctor elit sed egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla et ligula ullamcorper malesuada proin libero dignissim convallis aenean et tortor at risus nunc sed augue lacus viverra sed sed risus pretium quam vulputate dignissim suspendisse lectus arcu bibendum at varius vel quis imperdiet massa tincidunt nunc pulvinar sapien et sit amet cursus sit amet dictum sit amet justo donec iaculis nunc sed augue lacus viverra id venenatis a condimentum vitae sapien pellentesque habitant morbi tristique enim blandit volutpat maecenas volutpat neque vitae tempus quam pellentesque nec nam aliquam sit amet nisl suscipit adipiscing bibendum tincidunt vitae semper quis lectus nulla at ullamcorper eget nulla facilisi etiam dignissim fim ja_deveria_ter_terminado'.split()
    palavras_para_imprimir = [p for p in palavras if p[0] == 'a']
    mock_input(palavras)
    run_program(program)

    stdout, _ = capsys.readouterr()
    resultado = [s for s in stdout.lower().strip().split('\n') if s]
    dica = ''
    if len(resultado) != len(palavras_para_imprimir):
        dica = f'\nSeu programa imprimiu uma quantidade de palavras diferente do esperado. Confira se você está armazenando todos os inputs começados por a.'
        if len(resultado) == 1:
            dica = f'\nProvavelmente, você só perguntou uma vez...'
    assert resultado == palavras_para_imprimir, f'Algo deu errado na hora de imprimir somente as palavras iniciadas em a.{dica}'


@pytest.mark.timeout(5)
def test_somente_com_a_palavra_fim(capsys, mock_input, run_program):
    palavras = 'fim ja_deveria_ter_terminado'.split()
    palavras_para_imprimir = []
    mock_input(palavras)
    run_program(program)

    stdout, _ = capsys.readouterr()
    resultado = [s for s in stdout.lower().strip().split('\n') if s]
    dica = f'\nEste teste possui tem como primeiro input a palavra fim, ou seja, seu programa não deve imprimir nada. Confira o porquê você está imprindo as seguintes palavras: {resultado}'
    assert resultado == palavras_para_imprimir, f'Algo deu errado na hora de imprimir somente as palavras iniciadas em a.{dica}'


@pytest.mark.timeout(5)
def test_nenhuma_começa_com_a(capsys, mock_input, run_program):
    palavras = 'batman flash cyborg mulher_maravilha superman shazam lanterna_verde besouro_azul fim ja_deveria_ter_terminado'.split()
    palavras_para_imprimir = []
    mock_input(palavras)
    run_program(program)

    stdout, _ = capsys.readouterr()
    resultado = [s for s in stdout.lower().strip().split('\n') if s]
    dica = f'\nEste teste não possui nenhuma palavra que começa com a, portanto nada deve ser impresso. Confira o porquê você está imprindo as seguintes palavras: {resultado}'
    assert resultado == palavras_para_imprimir, f'Algo deu errado na hora de imprimir somente as palavras iniciadas em a.{dica}'


@pytest.mark.timeout(5)
def test_todos_começam_com_a(capsys, mock_input, run_program):
    palavras = 'atom atrocitus azrael aqualad arsenal amazo arqueiro_verde anarky aquaman fim ja_deveria_ter_terminado'.split()
    palavras_para_imprimir = [p for p in palavras if p[0] == 'a']
    mock_input(palavras)
    run_program(program)

    stdout, _ = capsys.readouterr()
    resultado = [s for s in stdout.lower().strip().split('\n') if s]
    dica = f'\nEste teste possui todas as suas palavras, exceto fim, iniciadas pela letra a. Confira o porquê está faltando alguma(s) delas.'
    assert resultado == palavras_para_imprimir, f'Algo deu errado na hora de imprimir somente as palavras iniciadas em a.{dica}'
