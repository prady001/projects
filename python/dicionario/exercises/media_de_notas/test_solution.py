import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_media
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_media')


def test_dicionarios_de_poucos_alunos():
    lista_dicionarios, media_correta, media_quase_correta = [{"aluno1": 5, "aluno2": 8}, {"aluno3": 5}], 6, 5.75
    resultado = calcula_media(lista_dicionarios)
    dica = ''
    if media_quase_correta == resultado:
        dica = 'DICA: O resultado é a média de todos os alunos, sem considerar as turmas.'
    assert resultado == media_correta, f'Algo deu errado na hora de calcular o {lista_dicionarios}.\nEra esperado {media_correta}, mas foi obtido {resultado}.\n{dica}'  


def test_dicionarios_de_muitos_alunos():
    lista_dicionarios, media_correta, media_quase_correta = [{"aluno1": 10.0, "aluno2": 8.0, "aluno3": 8.0, "aluno4": 9.5, "aluno5": 7.5}, {"alunoa": 7.0, "alunob": 4.5, "alunoc": 6.5, "alunod": 8.5, "alunoe": 7.0,}, {"alunoA": 10.0,"alunoB": 9.5}], 8, 8.35
    resultado = calcula_media(lista_dicionarios)
    dica = ''
    if media_quase_correta == resultado:
        dica = 'DICA: O resultado é a média de todos os alunos, sem considerar as turmas.'
    assert resultado == media_correta, f'Algo deu errado na hora de calcular o {lista_dicionarios}.\nEra esperado {media_correta}, mas foi obtido {resultado}.\n{dica}'  
