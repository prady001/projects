import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import eh_crescente
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'eh_crescente')


def test_lista_vazia():
    test_list = []
    expected = True
    response = eh_crescente(test_list)
    assert expected == response, f'Não funcionou para a entrada {test_list}, era esperado: {expected}.'


def test_um_digito():
    test_list = [1]
    expected = True
    response = eh_crescente(test_list)
    assert expected == response, f'Não funcionou para a entrada {test_list}, era esperado: {expected}.'


@pytest.mark.parametrize('list, expected',[
    pytest.param([1, 1], False, id='lista=[1, 1]'),
    pytest.param([1, 1, 1], False, id='lista=[1, 1, 1]'),
    pytest.param([1, 1, 2, 2], False, id='lista=[1, 1, 2, 2]'),
])
def test_digitos_iguais(list, expected):
    response = eh_crescente(list)
    assert expected == response, f'Não funcionou para a entrada {list}, era esperado: {expected}.'


@pytest.mark.parametrize('list, expected',[
    pytest.param([1, 2], True, id='lista=[1, 2]'),
    pytest.param([1, 2, 5], True, id='lista=[1, 2, 5]'),
    pytest.param([1, 2, 5, 20], True, id='lista=[1, 2, 5, 20]'),
    pytest.param([-1, 0, 1, 2, 5], True, id='lista=[-1, 0, 1, 2, 5]'),
    pytest.param([-10, -1, 0, 1, 2, 5, 15, 30], True, id='lista=[-10, -1, 0, 1, 2, 5, 15, 30]'),
])
def test_lista_crescente(list, expected):
    response = eh_crescente(list)
    assert expected == response, f'A lista {list} é crescente'


@pytest.mark.parametrize('list, expected',[
    pytest.param([2, 1], False, id='lista=[2, 1]'),
    pytest.param([10, 1], False, id='lista=[10, 1]'),
    pytest.param([1, -1], False, id='lista=[1, -1]'),
    pytest.param([1, 2, 3, 4, 5, 2], False, id='lista=[1, 2, 3, 4, 5, 2]'),
    pytest.param([-10, -1, 0, 1, 5, 3, 15, 30], False, id='lista=[-10, -1, 0, 1, 5, 3, 15, 30]'),
])
def test_lista_nao_crescente(list, expected):
    response = eh_crescente(list)
    assert expected == response, f'A lista {list} não é crescente'
