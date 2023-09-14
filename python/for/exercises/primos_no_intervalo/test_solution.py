from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import primos_entre
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'primos_entre')



def test_a_b_do_exemplo():
    a, b = 0, 12
    lista_primos = [2, 3, 5, 7, 11]
    resultado = primos_entre(a, b)
    assert resultado == lista_primos, f'Algo deu errado na hora de obter a lista de primos entre {a} e {b}.\nEra esperado {lista_primos}, mas foi obtido {resultado}.'


def test_a_maior_que_b():
    a, b = 10, 9
    lista_primos = []
    resultado = primos_entre(a, b)
    assert resultado == lista_primos, f'Algo deu errado na hora de obter a lista de primos entre {a} e {b}.\nEra esperado {lista_primos}, mas foi obtido {resultado}.'


def test_a_negativo():
    a, b = -4, 9
    lista_primos = [2, 3, 5, 7]
    resultado = primos_entre(a, b)
    assert resultado == lista_primos, f'Algo deu errado na hora de obter a lista de primos entre {a} e {b}.\nEra esperado {lista_primos}, mas foi obtido {resultado}.'


def test_muitos_primos_entre_a_b():
    a, b = 50, 100
    lista_primos = [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    resultado = primos_entre(a, b)
    assert resultado == lista_primos, f'Algo deu errado na hora de obter a lista de primos entre {a} e {b}.\nEra esperado {lista_primos}, mas foi obtido {resultado}.'


def test_nenhum_primo_entre_a_b():
    a, b = 54, 58
    lista_primos = []
    resultado = primos_entre(a, b)
    assert resultado == lista_primos, f'Algo deu errado na hora de obter a lista de primos entre {a} e {b}.\nEra esperado {lista_primos}, mas foi obtido {resultado}.'


def test_primos_entre_dois_primos():
    a, b = 13, 17
    lista_primos = [13, 17]
    resultado = primos_entre(a, b)
    assert resultado == lista_primos, f'Algo deu errado na hora de obter a lista de primos entre {a} e {b}.\nEra esperado {lista_primos}, mas foi obtido {resultado}.'
