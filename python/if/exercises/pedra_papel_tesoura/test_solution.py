import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import pedra_papel_tesoura
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'pedra_papel_tesoura')


@pytest.mark.parametrize('jogada, resposta', [
    (('pedra', 'pedra'), 'empate'),
    (('pedra', 'pedra'), 'empate'),
    (('pedra', 'pedra'), 'empate')
    ])
def test_empates(jogada, resposta):
    resultado = pedra_papel_tesoura(jogada[0], jogada[1])
    assert resultado == resposta, f'Não funcionou para ({jogada[0]}, {jogada[1]}).\nO esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.parametrize('jogada, resposta', [
    (('tesoura','papel'), 'um'),
    (('papel','pedra'), 'um'),
    (('pedra', 'tesoura'), 'um')
    ])
def test_jogador_um_vencedor(jogada, resposta):
    resultado = pedra_papel_tesoura(jogada[0], jogada[1])
    assert resultado == resposta, f'Não funcionou para ({jogada[0]}, {jogada[1]}).\nO esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.parametrize('jogada, resposta', [
    (('tesoura','pedra'), 'dois'),
    (('papel','tesoura'), 'dois'),
    (('pedra', 'papel'), 'dois')
    ])
def test_jogador_dois_vencedor(jogada, resposta):
    resultado = pedra_papel_tesoura(jogada[0], jogada[1])
    assert resultado == resposta, f'Não funcionou para ({jogada[0]}, {jogada[1]}).\nO esperado era {resposta}, mas foi obtido {resultado}!'


@pytest.mark.parametrize('jogada, resposta', [
    (('abcd','efgh'), 'Escolha pedra, papel ou tesoura para jogar'),
    (('papel','abcd'), 'Escolha pedra, papel ou tesoura para jogar'),
    (('abcd', 'papel'), 'Escolha pedra, papel ou tesoura para jogar')
    ])
def test_entrada_diferente_do_esperado(jogada, resposta):
    resultado = pedra_papel_tesoura(jogada[0], jogada[1])
    assert resultado == resposta, f'Não funcionou para ({jogada[0]}, {jogada[1]}).\nO esperado era {resposta}, mas foi obtido {resultado}!'
