from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import subtracao_de_listas
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'subtracao_de_listas')


def test_listas_do_exemplo():
    lista1, lista2 = [2, 7, 3.1, 'banana'], [2, 'banana', 'carro']
    lista_subtraida = [7, 3.1]
    resultado = subtracao_de_listas(lista1, lista2)
    assert len(resultado) == len(lista_subtraida), f'Algo deu errado ao comparar a quantidade de elementos da lista esperada {lista_subtraida} com o que foi obtido {resultado}.'
    for elemento in resultado:
        assert elemento in lista_subtraida, f'Está faltando elementos esperados na sua lista.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
    for elemento in lista_subtraida:
        assert elemento in resultado, f'Sua lista possui elementos que não eram esperados.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'


def test_duas_listas_vazias():
    lista1, lista2 = [], []
    lista_subtraida = []
    resultado = subtracao_de_listas(lista1, lista2)
    assert len(resultado) == len(lista_subtraida), f'Algo deu errado ao comparar a quantidade de elementos da lista esperada {lista_subtraida} com o que foi obtido {resultado}.'
    for elemento in resultado:
        assert elemento in lista_subtraida, f'Está faltando elementos esperados na sua lista.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
    for elemento in lista_subtraida:
        assert elemento in resultado, f'Sua lista possui elementos que não eram esperados.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'


def test_primeira_lista_vazia():
    lista1, lista2 = [], [1, 2, 3]
    lista_subtraida = []
    resultado = subtracao_de_listas(lista1, lista2)
    assert len(resultado) == len(lista_subtraida), f'Algo deu errado ao comparar a quantidade de elementos da lista esperada {lista_subtraida} com o que foi obtido {resultado}.'
    for elemento in resultado:
        assert elemento in lista_subtraida, f'Está faltando elementos esperados na sua lista.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
    for elemento in lista_subtraida:
        assert elemento in resultado, f'Sua lista possui elementos que não eram esperados.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'


def test_segunda_lista_vazia():
    lista1, lista2 = [1, 2, 3], []
    lista_subtraida = [1, 2, 3]
    resultado = subtracao_de_listas(lista1, lista2)
    assert len(resultado) == len(lista_subtraida), f'Algo deu errado ao comparar a quantidade de elementos da lista esperada {lista_subtraida} com o que foi obtido {resultado}.'
    for elemento in resultado:
        assert elemento in lista_subtraida, f'Está faltando elementos esperados na sua lista.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
    for elemento in lista_subtraida:
        assert elemento in resultado, f'Sua lista possui elementos que não eram esperados.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'


def test_listas_somente_de_inteiros():
    lista1, lista2 = [2, 0, 4, 9], [2, 9]
    lista_subtraida = [0, 4]
    resultado = subtracao_de_listas(lista1, lista2)
    assert len(resultado) == len(lista_subtraida), f'Algo deu errado ao comparar a quantidade de elementos da lista esperada {lista_subtraida} com o que foi obtido {resultado}.'
    for elemento in resultado:
        assert elemento in lista_subtraida, f'Está faltando elementos esperados na sua lista.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
    for elemento in lista_subtraida:
        assert elemento in resultado, f'Sua lista possui elementos que não eram esperados.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'


def test_listas_somente_de_strings():
    lista1, lista2 = ['godspeed', 'flash', 'kid_flash', 'capitao_frio', 'capitao_bumerangue', 'nevasca', 'flash_reverso'], ['flash_reverso', 'godspeed', 'capitao_frio', 'capitao_bumerangue', 'nevasca']
    lista_subtraida = ['flash', 'kid_flash']
    resultado = subtracao_de_listas(lista1, lista2)
    assert len(resultado) == len(lista_subtraida), f'Algo deu errado ao comparar a quantidade de elementos da lista esperada {lista_subtraida} com o que foi obtido {resultado}.'
    for elemento in resultado:
        assert elemento in lista_subtraida, f'Está faltando elementos esperados na sua lista.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
    for elemento in lista_subtraida:
        assert elemento in resultado, f'Sua lista possui elementos que não eram esperados.\nEra esperado {lista_subtraida}, mas foi obtido {resultado}.'
