import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import eh_palindromo
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'eh_palindromo')


@pytest.mark.parametrize('string, expected',[
    pytest.param('arara', True, id=f'string = "arara"'),
    pytest.param('Arara', True, id=f'string = "Arara"'),
    pytest.param('roma é amor', True, id=f'string = "roma é amor"'),
    pytest.param('abcddcba', True, id=f'string = "abcddcba"'),
    pytest.param('B', True, id=f'string = "B"'),
])
def test_strings_palindromas(string, expected):
    response = eh_palindromo(string)
    assert response == expected, f'A string "{string}" é palindroma.'


@pytest.mark.parametrize('string, expected',[
    pytest.param('roma não é amor', False, id=f'string = "roma não é amor"'),
    pytest.param('AB', False, id=f'string = "AB"'),
    pytest.param('abacate', False, id=f'string = "abacate"'),
    pytest.param('abcdabcd', False, id=f'string = "abcdabcd"'),
])
def test_strings_nao_palindromas(string, expected):
    response = eh_palindromo(string)
    assert response == expected, f'A string "{string}" não é palindroma.'
