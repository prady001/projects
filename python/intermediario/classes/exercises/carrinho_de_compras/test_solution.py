import solution as solucao
import pytest
import inspect


def test_existe_classe_carrinho():
    classe_existe = False
    if 'Carrinho' in inspect.getmembers(solucao)[0]:
        classe_existe = True
    assert classe_existe, 'A classe "Carrinho" não existe. Verifique que nomeou-a corretamente, com o "C" estando maiúsculo.'


def test_classe_carrinho_tem_metodos_adiciona_e_total_do_produto():
    metodo_adiciona_existe = False
    metodo_total_do_produto_existe = False
    carrinho = solucao.Carrinho()
    if hasattr(carrinho, 'adiciona'):
        metodo_adiciona_existe = True
    if hasattr(carrinho, 'total_do_produto'):
        metodo_total_do_produto_existe = True
    if not metodo_adiciona_existe and not metodo_total_do_produto_existe:
        raise AssertionError('A classe "Carrinho" não possui o método "adiciona" nem o método "total_do_produto", verifique que os definiu corretamente.')
    assert metodo_adiciona_existe, 'A classe "Carrinho" não possui um método chamado "adiciona", verifique que definiu uma função dentro da classe com esse nome.'
    assert metodo_total_do_produto_existe, 'A classe "Carrinho" não possui um método chamado "total_do_produto", verifique que definiu uma função dentro da classe com esse nome.'


def test_metodo_total_do_produto_retorna_zero_quando_produto_nao_esta_no_carrinho():
    carrinho = solucao.Carrinho()
    try:
        obtido = carrinho.total_do_produto('banana')
    except KeyError:
        raise AssertionError('O método "total_do_produto" está gerando um erro quando o produto não está no carrinho. Verifique que está tratando corretamente esse caso.')
    esperado = 0
    assert obtido == esperado, f'Algo deu errado, era esperado que o valor total fosse {esperado}, mas foi obtido {obtido}. Verifique que esta retornando o valor correto quando o produto não está no carrinho.'


def test_metodo_adiciona_coloca_produto_no_carrinho():
    carrinho = solucao.Carrinho()
    carrinho.adiciona('torta', 7)
    obtido = carrinho.total_do_produto('torta')
    esperado = 7
    assert obtido == esperado, f'Algo deu errado, era esperado que o valor total fosse {esperado}, mas foi obtido {obtido}. Verifique que esta adicionando os produtos corretamente ao dicionario.'


def test_metodo_adiciona_nao_sobrescreve_chave_e_valor():
    carrinho = solucao.Carrinho()
    carrinho.adiciona('maçã', 10)
    carrinho.adiciona('maçã', 15)
    obtido = carrinho.total_do_produto('maçã')
    esperado = 25
    assert obtido == esperado, f'Algo deu errado, era esperado que o valor total fosse {esperado}, mas foi obtido {obtido}. \n Fique atento para que quando um produto que já estava no carrinho for adicionado novamente, que o valor seja somado e não substitua o que já estava no dicionário.'
