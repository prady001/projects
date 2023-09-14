import solution as solucao
import pytest
import inspect


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_existe_classe_retangulo():
    classe_existe = False
    if 'Retangulo' in inspect.getmembers(solucao)[1]:
        classe_existe = True
    assert classe_existe, 'A classe "Retangulo" não existe. Verifique que nomeou-a corretamente, com o "R" estando maiúsculo.'


def test_retangulo_recebe_apenas_self_e_dois_pontos_em_init():
    try:
        p1 = Ponto(0,0)
        p2 = Ponto(2,2)
        retangulo = solucao.Retangulo(p1, p2)
    except TypeError as e:
        print(str(e))
        if '3 were given' in str(e):
            raise AssertionError('Número de argumentos do "__init__" está incorreto. Deveria receber três argumentos (incluindo o self).')
        else:
            raise e 


def test_classe_Retangulo_tem_metodos_para_calcular_perimetro_e_area():
    metodo_calcula_perimetro_existe = False
    metodo_calcula_area_existe = False
    p1 = Ponto(0,0)
    p2 = Ponto(2,2)
    retangulo = solucao.Retangulo(p1, p2)
    if hasattr(retangulo, 'calcula_perimetro'):
        metodo_calcula_perimetro_existe = True
    if hasattr(retangulo, 'calcula_area'):
        metodo_calcula_area_existe = True
    if not metodo_calcula_area_existe and not metodo_calcula_perimetro_existe:
        raise AssertionError('A classe "Retângulo" não possui o método "calcula_perimetro" nem o método "calcula_area", verifique que os definiu corretamente.')
    assert metodo_calcula_perimetro_existe, 'A classe "Retângulo" não possui um método chamado "calcula_perimetro", verifique que definiu uma função dentro da classe com esse nome.'
    assert metodo_calcula_area_existe, 'A classe "Retângulo" não possui um método chamado "calcula_area", verifique que definiu uma função dentro da classe com esse nome.'


def test_calcula_perimetro_corretamente():
    p1 = Ponto(0,0)
    p2 = Ponto(2,2)
    retangulo = solucao.Retangulo(p1, p2)
    perimetro = retangulo.calcula_perimetro()
    esperado = 8
    assert perimetro == esperado, f'O perímetro não é calculado corretamente, era esperado que o método retornasse {esperado}, mas foi obtido {perimetro}.'


def test_calcula_area_corretamente():
    p1 = Ponto(4,3)
    p2 = Ponto(7,9)
    retangulo = solucao.Retangulo(p1, p2)
    area = retangulo.calcula_area()
    esperado = 18
    assert area == esperado, f'A área não é calculada corretamente, era esperado que o método retornasse {esperado}, mas foi obtido {area}.'


def test_mais_de_um_Retangulo():
    p1 = Ponto(2,1)
    p2 = Ponto(4,3)
    Retangulo_1 = solucao.Retangulo(p1, p2)
    p3 = Ponto(5,7)
    p4 = Ponto(10,17)
    Retangulo_2 = solucao.Retangulo(p3, p4)
    perimetro_1 = Retangulo_1.calcula_perimetro()
    perimetro_2 = Retangulo_2.calcula_perimetro()
    area_1 = Retangulo_1.calcula_area()
    area_2 = Retangulo_2.calcula_area()
    esperado_perimetro_1 = 8
    esperado_perimetro_2 = 30
    esperado_area_1 =  4
    esperado_area_2 = 50
    assert perimetro_1 == esperado_perimetro_1, f'Algo deu errado nos cálculos do perímetro do primeiro Retângulo quando mais de 1 Retângulo é criado, era esperado {esperado_perimetro_1}, mas foi obtido {perimetro_1}, verifique que não utilizou variáveis globais.'
    assert perimetro_2 == esperado_perimetro_2, f'Algo deu errado nos cálculos do perímetro do segundo Retângulo quando mais de 1 Retângulo é criado, era esperado {esperado_perimetro_2}, mas foi obtido {perimetro_2}, verifique que não utilizou variáveis globais.'
    assert area_1 == esperado_area_1, f'Algo deu errado nos cálculos da área do primeiro Retângulo quando mais de 1 Retângulo é criado, era esperado {esperado_area_1}, mas foi obtido {perimetro_1}, verifique que não utilizou variáveis globais.'
    assert area_2 == esperado_area_2, f'Algo deu errado nos cálculos da área do segundo Retângulo quando mais de 1 Retângulo é criado, era esperado {esperado_area_2}, mas foi obtido {perimetro_2}, verifique que não utilizou variáveis globais.'
