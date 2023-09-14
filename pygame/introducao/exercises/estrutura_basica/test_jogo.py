from unittest import mock

try:
    import funcoes
except ModuleNotFoundError:
    pass

try:
    import pygame
except ModuleNotFoundError:
    pass

from pytest_devlife.util import *
from pytest_devlife.fixtures import mockgame

@mockgame(module_name='funcoes.pygame')
def test_1_inicializacao(mockgame):
    function_exists_in_module(funcoes, 'inicializa')

    window_to_be_returned = {}
    mockgame.display.set_mode.return_value = window_to_be_returned

    window = funcoes.inicializa()

    called_once_with(mockgame.init, [], {})
    called_once_with(mockgame.display.set_mode, ((320, 240),), {})
    assert id(window) == id(window_to_be_returned), 'inicializa deve retornar a janela criada'

    fake_substr = mock.MagicMock()
    fake_substr.__repr__ = mock.Mock(return_value='String començando com "Jogo d"')
    fake_substr.__eq__.side_effect = lambda s: s.startswith('Jogo d')

    called_once_with(mockgame.display.set_caption, (fake_substr,))


@mockgame('funcoes.pygame')
def test_2_recebe_eventos_QUIT(mockgame):
    function_exists_in_module(funcoes, 'recebe_eventos')

    mockgame.event.get.side_effect = [
        [pygame.event.Event(pygame.QUIT, {})]
    ]

    deve_continuar = funcoes.recebe_eventos()

    called_once_with(mockgame.event.get, [], {})
    assert deve_continuar == False, 'A função recebeu o evento de saída, mas retornou que o jogo deve continuar '


@mockgame('funcoes.pygame')
def test_2_recebe_eventos_sem_eventos(mockgame):
    function_exists_in_module(funcoes, 'recebe_eventos')

    mockgame.event.get.return_value = []

    deve_continuar = funcoes.recebe_eventos()

    called_once_with(mockgame.event.get, [], {})
    assert deve_continuar == True, 'A função não recebeu nenhum evento, mas retornou que o jogo deve parar'

@mockgame('funcoes.pygame')
def test_3_desenha_na_tela(mockgame):
    function_exists_in_module(funcoes, 'desenha')

    window = mock.MagicMock()
    funcoes.desenha(window)

    called_once_with(window.fill, ((255, 0, 0), ), {})
    called_once_with(mockgame.display.update, [], {})


@mockgame('funcoes.pygame')
def test_4_game_loop_chama_funcoes_criadas(mockgame):
    function_exists_in_module(funcoes, 'game_loop')
    function_exists_in_module(funcoes, 'desenha')
    function_exists_in_module(funcoes, 'recebe_eventos')

    win = mock.MagicMock()
    with mock.patch('funcoes.recebe_eventos') as recebe_mock:
        recebe_mock.side_effect = [True, False]
        with mock.patch('funcoes.desenha') as desenha_mock:

            funcoes.game_loop(win)

            called_once_with(desenha_mock, [win])
            assert all([len(args) == 0 for (args, _) in recebe_mock.call_args_list])
            assert len(recebe_mock.call_args_list) == 2

            assert len(mockgame.quit.call_args_list) == 0, 'pygame.quit não deve ser chamada nessa função'


@mockgame('funcoes.pygame')
def test_4_game_loop_roda_4_vezes_antes_de_sair(mockgame):
    function_exists_in_module(funcoes, 'game_loop')

    mockgame.event.get.side_effect = [
        [],[],[],
        [pygame.event.Event(pygame.QUIT, {})]
    ]

    window = mock.MagicMock()
    with catch_loop_stop_iteration():
        funcoes.game_loop(window)

    n_calls_update = len(mockgame.display.update.call_args_list)
    assert n_calls_update >= 3 and n_calls_update < 4, 'pygame.display.update deveria ser chamada no máximo 4 vezes'
    assert len(mockgame.event.get.mock_calls) == 4, 'pygame.display.update deveria ser chamada exatamente 4 vezes'


@mockgame('funcoes.pygame')
def test_4_game_loop_sai_na_primeira_vez(mockgame):
    function_exists_in_module(funcoes, 'game_loop')

    mockgame.event.get.side_effect = [
        [pygame.event.Event(pygame.QUIT, {})]
    ]

    window = mock.MagicMock()
    with catch_loop_stop_iteration():
        funcoes.game_loop(window)

    assert len(mockgame.display.update.mock_calls) < 1, 'pygame.display.update deveria ser chamada no máximo 1 vez'
    assert len(mockgame.event.get.mock_calls) == 1, 'pygame.display.update deveria ser chamada exatamente 1 vez'


@mockgame('funcoes.pygame')
def test_4_game_loop_sai_na_segunda_vez(mockgame):
    function_exists_in_module(funcoes, 'game_loop')

    mockgame.event.get.side_effect = [
        [pygame.event.Event(pygame.KEYDOWN, {})],
        [pygame.event.Event(pygame.QUIT, {})]
    ]

    window = mock.MagicMock()
    with catch_loop_stop_iteration():
        funcoes.game_loop(window)

    assert len(mockgame.display.update.mock_calls) < 2, 'pygame.display.update deveria ser chamada no máximo 2 vezes'
    assert len(mockgame.event.get.mock_calls) == 2, 'pygame.display.update deveria ser chamada exatamente 2 vezes'
