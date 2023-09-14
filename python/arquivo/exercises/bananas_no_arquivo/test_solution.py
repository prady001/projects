import pytest
from pathlib import Path


PWD = Path(__file__).parent
program = PWD / 'solution.py'


def test_programa_reconhece_banana(capsys, tmp_path, mock_input, run_program):
    CONTENT = 'banana'
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / "macacos-me-mordam.txt"
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    esperado = 1
    captured = int(capsys.readouterr().out)
    assert captured == esperado, f'Algo deu de errado, seu programa não reconheceu a palavra "banana". Era esperado {esperado}, mas foi obtido {captured}'


def test_programa_reconhece_banana_com_letras_maiusculas(capsys, tmp_path, mock_input, run_program):
    CONTENT = 'BaNana BANANA bAnAnA'
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / 'macacos-me-mordam.txt'
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    esperado = 3
    captured = int(capsys.readouterr().out)
    assert captured == esperado, f'Algo deu de errado, seu programa não reconheceu a palavra "banana" quando continha alguma ou todas as letras maiúsculas. Era esperado {esperado}, mas foi obtido {captured}'


def test_programa_reconhece_banana_com_pontuacao(capsys, tmp_path, mock_input, run_program):
    CONTENT = 'banana. Banana? Banana, BANANA! banana; "Banana"'
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / 'macacos-me-mordam.txt'
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    esperado = 6
    captured = int(capsys.readouterr().out)
    assert captured == esperado, f'Algo deu de errado, seu programa não reconheceu a palavra "banana" quando estava acompanhada de pontuação. Era esperado {esperado}, mas foi obtido {captured}'


def test_programa_nao_reconhece_banana_com_letras_a_mais(capsys, tmp_path, mock_input, run_program):
    CONTENT = 'bananas Bananaaaa Bananada BANANA1'
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / 'macacos-me-mordam.txt'
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    esperado = 0
    captured = int(capsys.readouterr().out)
    assert captured == esperado, f'Algo deu de errado, seu programa reconheceu palavras com a base "banana" seguidas de mais letras. Era esperado {esperado}, mas foi obtido {captured}'


def test_texto_contendo_bananas(capsys, tmp_path, mock_input, run_program):
    CONTENT = 'Ontem fui ao supermercado e encontrei a ala das bananas. Lá tinha a maior banana nanica que já vi na minha vida fiquei com uma vontada de pegar algumas para fazer uma bananada, mas no final são só bananas. Banana prata também tinha mas tava cara, como assim tu viu a carla vestida de BANANA!?'
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / 'macacos-me-mordam.txt'
    p.write_text(CONTENT)
    mock_input([str(p)])
    run_program(program)
    esperado = 3
    captured = int(capsys.readouterr().out)
    assert captured == esperado, f'Algo deu de errado, seu programa não encontrou o número correto, de "banana" no texto. Era esperado {esperado}, mas foi obtido {captured}'
