import pytest
import re
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


def test_programa_não_conta_espaço_vazio(capsys, tmp_path, mock_input, run_program):
    CONTENT = "olá tchau"
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / "texto.txt"
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    captured = capsys.readouterr().out
    if captured != '':
        temp = re.findall(r'\d+', captured)
        obtido = list(map(int, temp))[0]
        esperado = 2
        assert obtido == esperado, f'Algo deu de errado, era esperado que fossem contadas {esperado} palavras, mas foram contada(s) {obtido}. Verifique que desconsidera o espaço entre palavras."'
    else:
        assert False, 'Algo deu de errado, seu programa não imprimiu o número de palavras.'


def test_conta_palavras_corretamente(capsys, tmp_path, mock_input, run_program):
    CONTENT = "Minha terra tem palmeiras \nOnde canta o Sabiá \nAs aves que aqui gorjeiam \n Não gorjeiam como lá"
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / "texto.txt"
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    captured = capsys.readouterr().out
    if captured != '':
        temp = re.findall(r'\d+', captured)
        obtido = list(map(int, temp))[0]
        esperado = 17
        assert obtido == esperado, f'Algo deu de errado quando contando o número de palavras, era esperado que fossem contadas {esperado} palavras, mas foi obtido {obtido} palavras."'
    else:
        assert False, 'Algo deu de errado, seu programa não imprimiu o número de palavras.'
