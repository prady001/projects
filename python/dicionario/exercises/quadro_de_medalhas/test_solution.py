from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import pais_campeao
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'pais_campeao')


ENTRADA1 = {
    'China': {
        'ouro': 20,
        'prata': 35,
        'bronze': 40
    },
    'Canadá': {
        'ouro': 5,
        'prata': 15,
        'bronze': 20
    },
    'Estados Unidos': {
        'ouro': 25,
        'prata': 35,
        'bronze': 40
    },
    'Brasil': {
        'ouro': 10,
        'prata': 10,
        'bronze': 8
    }}

ENTRADA2 = {
    'México': {
        'ouro': 0,
        'prata': 3,
        'bronze': 2
    },
    'Malásia': {
        'ouro': 0,
        'prata': 4,
        'bronze': 1
    },
    'Argélia': {
        'ouro': 0,
        'prata': 2,
        'bronze': 0
    },
    'Irlanda': {
        'ouro': 0,
        'prata': 2,
        'bronze': 5
    }}

ENTRADA3 = {
    'Noruega': {
        'ouro': 1,
        'prata': 0,
        'bronze': 2
    },
    'Egito': {
        'ouro': 0,
        'prata': 4,
        'bronze': 1
    },
    'Áustria': {
        'ouro': 0,
        'prata': 4,
        'bronze': 0
    },
    'Tunísia': {
        'ouro': 1,
        'prata': 0,
        'bronze': 3
    }}


def test_dicionario_com_muitos_dicionarios():
    dica = ''
    saidas, esperados = [pais_campeao(ENTRADA1), pais_campeao(ENTRADA2), pais_campeao(ENTRADA3)], ['Estados Unidos', 'Malásia', 'Tunísia']
    for i in range(len(saidas)):
        saida, esperado = saidas[i], esperados[i]
        if type(saida) != str:
            dica = '\nAVISO: Sua função não está retornando uma string.\n'
        assert saida == esperado, f'\nAlgo deu errado na hora de verificar qual foi o país campeão.\nEra esperado {esperado}, mas foi obtido {saida}.\n{dica}'
