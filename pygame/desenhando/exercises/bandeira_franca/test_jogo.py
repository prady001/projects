from pathlib import Path
from unittest import mock

try:
    import pygame
    import jogo
except ModuleNotFoundError:
    pass

from pytest_devlife.fixtures import mockgame


def assert_surfaces(obtido, esperado, img):
    w1 = obtido.get_width()
    w2 = esperado.get_width()
    h1 = obtido.get_height()
    h2 = esperado.get_height()
    assert w1 == w2, f'A largura das imagens é diferente. Obtido: {w1}. Esperado: {w2}'
    assert h1 == h2, f'A altura das imagens é diferente. Obtido: {h1}. Esperado: {h2}'

    iguais = 0
    for x in range(w1):
        for y in range(h1):
            if obtido.get_at((x, y)) == esperado.get_at((x, y)):
                iguais += 1

    porcentagem_iguais = iguais / (w1 * h1)
    assert porcentagem_iguais > 0.9, f'Imagem diferente da esperada. Consulte o gabarito em: {img}'


def carrega_com_copia(img):
    gabarito = pygame.image.load(img)
    tela = gabarito.copy()
    tela.fill((0, 0, 0))
    return gabarito, tela


def test_desenha_bandeira():
    img = Path(__file__).parent / 'bandeira.png'
    gabarito, tela = carrega_com_copia(img)

    with mock.patch('jogo.pygame.display.update'):
        jogo.desenha(tela)
    pygame.image.save(tela, 'obtido.png')
    assert_surfaces(tela, gabarito, img)
