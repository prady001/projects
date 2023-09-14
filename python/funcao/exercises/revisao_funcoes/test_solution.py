from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import revisao_funcao
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'revisao_funcao')


def test_resultado_para_argumento_0():
    assert revisao_funcao(0) == 1


def test_resultado_para_argumento_1():
    assert revisao_funcao(1) == -1


def test_resultado_para_argumento_2():
    assert revisao_funcao(2) == 1


def test_resultado_para_argumento_3():
    assert revisao_funcao(3) == -1
