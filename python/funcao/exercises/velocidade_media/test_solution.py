import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_velocidade_media
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_velocidade_media')


def error_msg(km, h, hit, expected):
    return f'Era esperado o valor {expected}, mas foi obtido o valor {hit}'


def test_distancia_zero():
    km = 0
    h = 1
    expected = pytest.approx(0.0)
    hit = calcula_velocidade_media(km, h)
    assert hit == expected, error_msg(0, 1, hit, expected)


def test_distancia_e_tempo_iguais():
    km = 1
    h = 1
    expected = pytest.approx(1.0)
    hit = calcula_velocidade_media(km, h)
    assert hit == expected, error_msg(0, 1, hit, expected)


def test_tempo_float():
    km = 1
    h = 0.1
    expected = pytest.approx(10.0)
    hit = calcula_velocidade_media(km, h)
    assert hit == expected, error_msg(0, 1, hit, expected)


def test_distancia_float():
    km = 0.1
    h = 1
    expected = pytest.approx(0.1)
    hit = calcula_velocidade_media(km, h)
    assert hit == expected, error_msg(0, 1, hit, expected)


def test_velocidade_media_float():
    km = 1
    h = 2
    expected = pytest.approx(0.5)
    hit = calcula_velocidade_media(km, h)
    assert hit == expected, error_msg(0, 1, hit, expected)


def test_distancia_grande():
    km = 1098
    h = 9
    expected = pytest.approx(122.0)
    hit = calcula_velocidade_media(km, h)
    assert hit == expected, error_msg(0, 1, hit, expected)
