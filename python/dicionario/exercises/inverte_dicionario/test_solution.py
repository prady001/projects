from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import inverte_dicionario
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'inverte_dicionario')


def test_dicionario_vazio():
    entrada = {}
    esperado = {}
    obtido = inverte_dicionario(entrada)
    assert obtido == esperado, f'Algo deu errado na função para dicionarios vazios.\nEra esperado {esperado}, mas foi obtido {obtido}.'


def test_idades_iguais():
    entrada = {'Ana': 32, 'Bruno': 32, 'João': 32, 'Maria': 32, 'Enzo': 32, 'Joana': 32}
    esperado = {32: ['Ana', 'Bruno', 'João', 'Maria', 'Enzo', 'Joana']}
    obtido = inverte_dicionario(entrada)
    assert obtido == esperado, f'Algo deu errado para dicionarios de pessoas com a mesma idade.\nPara a entrada {entrada}, era esperado {esperado}, mas foi obtido {obtido}.'


def test_idades_diferentes():
    entrada = {'Ana': 15, 'Bruno': 30, 'João': 7, 'Maria': 62, 'Enzo': 18, 'Beatriz': 80}
    esperado = {7: ['João'], 15: ['Ana'], 18: ['Enzo'], 30: ['Bruno'], 62: ['Maria'], 80: ['Beatriz']}
    obtido = inverte_dicionario(entrada)
    assert obtido == esperado, f'Algo deu errado para dicionarios de pessoas de idades diferentes.\nPara a entrada {entrada}, era esperado {esperado}, mas foi obtido {obtido}.'


def test_idades_com_repeticoes():
    entrada = {'Ana': 19, 'Bruno': 18, 'João': 19, 'Letícia': 19}
    esperado = {18: ['Bruno'], 19: ['Ana', 'João', 'Letícia']}
    obtido = inverte_dicionario(entrada)
    assert obtido == esperado, f'Algo deu errado para dicionarios em que algumas idades se repetem.\nPara a entrada {entrada}, era esperado {esperado}, mas foi obtido {obtido}.'
