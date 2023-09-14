from unittest import mock
from pytest_devlife import util

try:
    import cotacoes
    cotacao_de_hoje = cotacoes.dolar()
except ImportError:
    cotacao_de_hoje = 0
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import preco_em_reais
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'preco_em_reais')


def test_preco_em_reais_1_dolar():
    preco_reais = preco_em_reais(1)
    assert preco_reais == cotacao_de_hoje


def test_preco_em_reais_0_dolar():
    preco_reais = preco_em_reais(0)
    assert preco_reais == 0


def test_preco_em_reais_5_dolar():
    preco_reais = preco_em_reais(5)
    assert preco_reais == cotacao_de_hoje * 5


def test_preco_em_reais_0_5_dolar():
    preco_reais = preco_em_reais(0.5)
    assert preco_reais == cotacao_de_hoje / 2


def test_chamou_funcao_dolar():
    function_name = 'cotacoes.dolar'
    if hasattr(solution, 'dolar'):
        function_name = 'solution.dolar'
    with mock.patch(function_name) as f:
        f.return_value = 3

        preco_reais = preco_em_reais(2)

        assert f.call_count == 1, 'cotacoes.dolar deve ser chamada exatamente uma vez'
        assert len(f.call_args_list[0].args) == 0, 'cotacoes.dolar deve ser chamada sem argumentos'
        assert preco_reais == 3 * 2
