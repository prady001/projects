from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import traduz
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'traduz')


def test_frutas():
    lista_frutas = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']
    dicionario_frutas = {
        'pineapple': 'abacaxi',
        'plum': 'ameixa',
        'blackberry': 'amora',
        'apple': 'maçã',
        'cashew': 'caju',
        'cherry': 'cereja'
    }
    resposta = ['amora', 'cereja', 'ameixa', 'maçã', 'abacaxi']
    resultado = traduz(lista_frutas, dicionario_frutas)
    assert resultado == resposta, f'Não funcionou para a lista {lista_frutas}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


def test_objetos_de_casa():
    lista_objetos_de_casa = ['house', 'mouse', 'mouse', 'plant']
    dicionario_objetos_de_casa = {
        'house': 'casa',
        'plant': 'planta',
        'mouse': 'rato',
        'desk': 'mesa'
    }
    resposta = ['casa', 'rato', 'rato', 'planta']
    resultado = traduz(lista_objetos_de_casa, dicionario_objetos_de_casa)
    assert resultado == resposta, f'Não funcionou para a lista {lista_objetos_de_casa}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


def test_conversa():
    lista_conversa = ['hi', 'what', 'why',
                      'because', 'but', 'much', 'excuse', 'please']
    dicionario_conversa = {
        'hi': 'oi',
        'because': 'pois',
        'what': 'o que',
        'why': 'porque',
        'but': 'mas',
        'please': 'por favor',
        'excuse': 'com licença',
        'color': 'cor',
        'much': 'muito',
        'car': 'carro',
        'dream': 'sonhe',
        'drink': 'bebida'
    }
    resposta = ['oi', 'o que', 'porque', 'pois',
                'mas', 'muito', 'com licença', 'por favor']
    resultado = traduz(lista_conversa, dicionario_conversa)
    assert resultado == resposta, f'Não funcionou para a lista {lista_conversa}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


def test_numeros():
    lista_numeros = ['one', 'two', 'three', 'four',
                     'five', 'six', 'seven', 'eight', 'nine', 'ten']
    dicionario_numeros = {
        'three': 'três',
        'haste': 'pressa',
        'two': 'dois',
        'six': 'seis',
        'dog': 'cão',
        'one': 'um',
        'hero': 'herói',
        'four': 'quatro',
        'eight': 'oito',
        'five': 'cinco',
        'nine': 'nove',
        'ten': 'dez',
        'brown': 'marrom',
        'seven': 'sete'
    }
    resposta = ['um', 'dois', 'três', 'quatro',
                'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
    resultado = traduz(lista_numeros, dicionario_numeros)
    assert resultado == resposta, f'Não funcionou para a lista {lista_numeros}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'


def test_comidas():
    lista_comidas = ['Salad', 'Beef', 'Chicken',
                     'Egg', 'Rice', 'Bean', 'Salt', 'Sugar']
    dicionario_comidas = {
        'Sugar': 'Açúcar',
        'haste': 'pressa',
        'two': 'dois',
        'Salad': 'Salada',
        'dog': 'cão',
        'Beef': 'Carne',
        'hero': 'herói',
        'four': 'quatro',
        'Chicken': 'Galinha',
        'five': 'cinco',
        'Egg': 'Ovo',
        'ten': 'dez',
        'Rice': 'Arroz',
        'Bean': 'Feijão',
        'Square': 'Praça',
        'Salt': 'Sal',
    }
    resposta = ['Salada', 'Carne', 'Galinha',
                'Ovo', 'Arroz', 'Feijão', 'Sal', 'Açúcar']
    resultado = traduz(lista_comidas, dicionario_comidas)
    assert resultado == resposta, f'Não funcionou para a lista {lista_comidas}\nO resultado esperado era {resposta}, mas foi obtido {resultado}!'
