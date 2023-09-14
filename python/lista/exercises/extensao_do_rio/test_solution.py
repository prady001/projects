import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_extensao
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_extensao')


x_arg = [[4, 7], [-9, -2, 2, 3, 8], [-10, -6, -3], [-2, -1, 7], [-9, -1, 6], [-4, -2, 1, 2, 3], [-10, -9, -6, 2], [-8, -3], [-6, -2], [-6, 0]]
y_arg = [[-2, -4], [7, -4, -6, 2, -4], [4, -3, 9], [-9, -4, -9], [3, -8, 5], [8, 9, -5, -4, -1], [5, -3, -5, 8], [-10, 3], [-4, 1], [-8, -2]]
ans = [3.61, 33.38, 20.43, 14.53, 28.37, 21.13, 26.93, 13.93, 6.40, 8.49]
@pytest.mark.timeout(5)
@pytest.mark.parametrize("x_list,y_list,expected",
    [
        pytest.param(x_arg[i], y_arg[i], ans[i], id = f"xs = {x_arg[i]}, ys = {y_arg[i]}") for i in range(len(x_arg))
    ]
)
def test_calcula_extensao_do_rio_para_coordenadas_(x_list, y_list, expected):
    ans = calcula_extensao(x_list, y_list)

    msg = f"O esperado para a extensão do rio era {expected:.2f}, mas recebemos {ans:.2f}."
    assert ans == pytest.approx(expected, rel = 1e-2), msg
