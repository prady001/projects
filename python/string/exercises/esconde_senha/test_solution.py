import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import esconde_senha
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'esconde_senha')


@pytest.mark.parametrize(
    'senha_visivel,senha_escondida',
    [
        pytest.param(visivel, escondida, id=visivel)
        for visivel, escondida in [
            ('batman', '******'),
            ('', ''),
            ('$&nh4!?', '*******'),
            ('*', '*'),
            ('charada?', '********'),
            ('PiNGu1n\\/', '*********'),
            ('*esconde*', '*********')
        ]
    ]
)


def test_esconde_a_senha(senha_visivel, senha_escondida):
    resultado = esconde_senha(senha_visivel)
    assert resultado == senha_escondida, f'O número de caracteres da entrada não é compatível com o da saída.\nDICA: para a entrada de {len(senha_visivel)} caracteres, sua função retorna {len(resultado)} caracteres.'
