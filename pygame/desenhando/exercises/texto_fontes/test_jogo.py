from pathlib import Path
from unittest import mock

try:
    import jogo
except ModuleNotFoundError:
    pass

def test_carregamento_fontes():
    with mock.patch('jogo.pygame') as mockg:
        mockg.font.get_default_font.side_effects = ['a', 'a']

        font1_mock = mock.Mock()
        font1_mock.render.return_value = 'OK1'
        font2_mock = mock.Mock()
        font2_mock.render.return_value = 'OK2'

        mockg.font.Font.side_effect = [
            font1_mock, font2_mock
        ]

        try:
            w, assets = jogo.inicializa()
        except (ValueError, TypeError):
            # Não retornou 2 elementos
            raise AssertionError('inicializa deverá retornar a janela criada (window) e o dicionário de recursos do jogo (assets)')

        assert type(assets) == dict, 'assets deve ser um dicionário.'
        for k in ['fonte_16', 'fonte_24']:
            assert k in assets, f'assets["{k}"] não existe'

        assert assets['fonte_16'] != assets['fonte_24'], 'fonte_16 e fonte_24 são idênticos'
        assert assets['fonte_16'] == font1_mock or assets['fonte_16'] == font2_mock, 'fonte_16 não foi criado usando pygame.font.Font'
        assert assets['fonte_24'] == font1_mock or assets['fonte_24'] == font2_mock, 'fonte_16 não foi criado usando pygame.font.Font'


def test_desenho_fontes():
    font16_render = mock.Mock()
    font16_mock = mock.Mock()
    font16_mock.render.return_value = font16_render

    font24_render = mock.Mock()
    font24_mock = mock.Mock()
    font24_mock.render.return_value = font24_render

    assets = {
        'fonte_16': font16_mock,
        'fonte_24': font24_mock,
    }
    window = mock.Mock()

    with mock.patch('jogo.pygame') as mockg:
        jogo.desenha(window, assets)

    assert assets['fonte_16'].render.mock_calls == [mock.call('Fonte tamanho 16', True, (255, 255, 255))], 'A chamada a render na fonte de tamanho 16 não foi feita com os argumentos corretos.'
    assert assets['fonte_24'].render.mock_calls == [mock.call('Fonte tamanho 24', True, (0, 0, 255))], 'A chamada a render na fonte de tamanho 16 não foi feita com os argumentos corretos.'

    assert mock.call(font16_render, (10, 20)) in window.blit.mock_calls, 'O desenho do texto de fonte 16 foi feito incorretamente'
    assert mock.call(font24_render, (10, 70)) in window.blit.mock_calls, 'O desenho do texto de fonte 24 foi feito incorretamente'
