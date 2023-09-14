from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import distancia_euclidiana
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'distancia_euclidiana')


def test_pontos_do_exemplo():
    x1, y1, x2, y2 = 8, 12, 4, 9
    distancia = 5
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    assert resultado == distancia, f'Algo deu errado na hora de verificar a distância entre os pontos ({x1},{y1}) e ({x2},{y2}).\nEra esperado {distancia}, mas foi obtido {resultado}.'


def test_ponto_na_origem():
    x1, y1, x2, y2 = 0, 0, 3, 4
    distancia = 5
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    assert resultado == distancia, f'Algo deu errado na hora de verificar a distância entre os pontos ({x1},{y1}) e ({x2},{y2}).\nEra esperado {distancia}, mas foi obtido {resultado}.'


def test_pontos_iguais():
    x1, y1, x2, y2 = 10, 4, 10, 4
    distancia = 0
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    assert resultado == distancia, f'Algo deu errado na hora de verificar a distância entre os pontos ({x1},{y1}) e ({x2},{y2}).\nEra esperado {distancia}, mas foi obtido {resultado}.'


def test_pontos_proximos_em_x():
    x1, y1, x2, y2 = 10, 0, 11, 0
    distancia = 1
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    assert resultado == distancia, f'Algo deu errado na hora de verificar a distância entre os pontos ({x1},{y1}) e ({x2},{y2}).\nEra esperado {distancia}, mas foi obtido {resultado}.'


def test_pontos_proximos_em_y():
    x1, y1, x2, y2 = 0, 5, 0, 4
    distancia = 1
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    assert resultado == distancia, f'Algo deu errado na hora de verificar a distância entre os pontos ({x1},{y1}) e ({x2},{y2}).\nEra esperado {distancia}, mas foi obtido {resultado}.'


def test_pontos_distantes_nos_dois_eixos():
    x1, y1, x2, y2 = 2, 3, 5, 7
    distancia = 5
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    assert resultado == distancia, f'Algo deu errado na hora de verificar a distância entre os pontos ({x1},{y1}) e ({x2},{y2}).\nEra esperado {distancia}, mas foi obtido {resultado}.'
