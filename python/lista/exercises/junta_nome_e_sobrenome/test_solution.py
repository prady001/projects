import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import nomes_completos
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'nomes_completos')


@pytest.mark.timeout(5)
def test_primeiro_nome_e_segundo_com_letras_minuscula():
    primeiros_nomes = ['joão', 'guilherme', 'amanda']
    sobrenomes = ['sousa', 'santos', 'borges']
    resposta = ['joão sousa', 'guilherme santos', 'amanda borges']
    resultado = nomes_completos(primeiros_nomes, sobrenomes)
    assert resultado == resposta, f'Algo deu errado na junção dos nomes.\nEra esperado {resposta}, mas retornou {resultado}!'


@pytest.mark.timeout(5)
def test_primeiro_nome_e_segundo_com_letras_maiusculas():
    primeiros_nomes = ['Carlos', 'Vitória', 'Sarah', 'Jorge']
    sobrenomes = ['Vasconcelos', 'Campos', 'Pimentel', 'Campinas']
    resposta = ['Carlos Vasconcelos', 'Vitória Campos', 'Sarah Pimentel', 'Jorge Campinas']
    resultado = nomes_completos(primeiros_nomes, sobrenomes)
    assert resultado == resposta, f'Algo deu errado na junção dos nomes.\nEra esperado {resposta}, mas retornou {resultado}!'


@pytest.mark.timeout(5)
def test_primeiro_nome_com_maiuscula_e_segundo_com_minuscula():
    primeiros_nomes = ['Jéssica', 'Camila', 'Ester', 'João', 'Alynne']
    sobrenomes = ['santos', 'souza', 'sampaio', 'silva', 'nogueira']
    resposta = ['Jéssica santos', 'Camila souza', 'Ester sampaio', 'João silva', 'Alynne nogueira']
    resultado = nomes_completos(primeiros_nomes, sobrenomes)
    assert resultado == resposta, f'Algo deu errado na junção dos nomes.\nEra esperado {resposta}, mas retornou {resultado}!'


@pytest.mark.timeout(5)
def test_primeiro_nome_com_minuscula_e_segundo_com_maiuscula():
    primeiros_nomes = ['jennifer', 'francisco', 'camilo', 'antônio', 'álvaro', 'ricardo']
    sobrenomes = ['Sales', 'Amorim', 'Mário', 'Pitolver', 'Marium', 'Vânio']
    resposta = ['jennifer Sales', 'francisco Amorim', 'camilo Mário', 'antônio Pitolver', 'álvaro Marium', 'ricardo Vânio']
    resultado = nomes_completos(primeiros_nomes, sobrenomes)
    assert resultado == resposta, f'Algo deu errado na junção dos nomes.\nEra esperado {resposta}, mas retornou {resultado}!'


@pytest.mark.timeout(5)
def test_primeiro_nome_com_minuscula_e_segundo_com_maiuscula():
    primeiros_nomes = ['SAULO', 'ARNON', 'EVELLYN']
    sobrenomes = ['QUEIROZ', 'SMITH', 'BORGES']
    resposta = ['SAULO QUEIROZ', 'ARNON SMITH', 'EVELLYN BORGES']
    resultado = nomes_completos(primeiros_nomes, sobrenomes)
    assert resultado == resposta, f'Algo deu errado na junção dos nomes.\nEra esperado {resposta}, mas retornou {resultado}!'
