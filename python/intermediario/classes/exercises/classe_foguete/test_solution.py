import solution as solucao
import pytest
import inspect


def test_existe_classe_foguete():
    classe_existe = False
    if 'Foguete' in inspect.getmembers(solucao)[0]:
        classe_existe = True
    assert classe_existe, 'A classe "Foguete" não existe. Verifique que nomeou-a corretamente, com o "F" estando maiúsculo.'


def test_foguete_recebe_apenas_self_e_velocidade_em_init():
    try:
        foguete = solucao.Foguete(10000)
    except TypeError as e:
        print(str(e))
        if '2 were given' in str(e):
            raise AssertionError('Número de argumentos do "__init__" está incorreto. Deveria receber dois argumentos (incluindo o self).')
        else:
            raise e 


def test_classe_foguete_tem_metodo_atualizar():
    metodo_atualizar_existe = False
    foguete = solucao.Foguete(10)
    if hasattr(foguete, 'atualizar'):
        metodo_atualizar_existe = True
    assert metodo_atualizar_existe, 'A classe "Foguete" não possui um método chamado "atualizar", verifique que definiu uma função dentro da classe com esse nome.'


def test_metodo_atualizar_recebe_tempo():
    try:
        foguete = solucao.Foguete(10000)
        foguete.atualizar(5)
    except TypeError as e:
        print(str(e))
        if '2 were given' in str(e):
            raise AssertionError('Número de argumentos do método "atualizar" está incorreto. Deveria receber dois argumentos (incluindo o self).')
        else:
            raise e


def test_saida_do_metodo_atualizar():
    foguete = solucao.Foguete(100)
    distancia = foguete.atualizar(3600)
    esperado = 100
    if distancia != None:
        assert distancia == esperado, f'O método "atualizar" não parece devolver o valor correto da distância percorrida. Era esperado {esperado}, mas foi obtido {distancia}, verifique que está fazendo os cálculos com o tempo em segundos e devolvendo o resultado em quilômetros.'
    else:    
        raise AssertionError('O método "atualizar" devolve nenhum valor, verique que ele possui um "return" com a distância percorrida.')


def test_acumula_distancia_percorrida():
    foguete = solucao.Foguete(100)
    for i in range(0,3):
        distancia = foguete.atualizar(3600)
    esperado = 300
    assert distancia == esperado, f'O método "atualizar" não acumula a distância percorrida depois de ser chamado várias vezes. Era esperado {esperado}, mas foi obtido {distancia}, verifique que a variável que define a distância na classe não é sobrescrita quando o método é chamado.'


def test_mais_de_um_foguete():
    foguete_1 = solucao.Foguete(450)
    foguete_2 = solucao.Foguete(932)
    distancia_1 = foguete_1.atualizar(1800)
    distancia_2 = foguete_2.atualizar(900)
    esperado_1 = 225
    esperado_2 = 233
    assert distancia_2 == esperado_2, f'Algo deu errado nos cálculos do primeiro foguete quando mais de 1 foguete é criado, era esperado {esperado_1}, mas foi obtido {distancia_1}, verifique que não utilizou variáveis globais.'
    assert distancia_1 == esperado_1, f'Algo deu errado nos cálculos do segundo foguete quando mais de 1 foguete é criado, era esperado {esperado_2}, mas foi obtido {distancia_2}, verifique que não utilizou variáveis globais.'
