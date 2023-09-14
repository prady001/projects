from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import verifica_preco
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'verifica_preco')


def test_do_exemplo():
    livros = {
                "Pinóquio": "azul",
                "Dom Quixote": "amarelo",
                "O Pequeno Príncipe": "vermelho",
            }
    cores = {
                "vermelho": 10.0,
                "azul": 20.0,
                "amarelo": 40.0,
                "verde": 100.0,
            }
    for titulo in livros:
        esperado = cores[livros[titulo]]
        obtido = verifica_preco(titulo, livros, cores)
        msg = f'Para o seguinte o livro {titulo}, era esperado {esperado} mas foi obtido {obtido}.\nO dicionário de cores utilizado foi {cores} e o de preços foi {livros}.'
        assert esperado == obtido, msg


def test_muitos_livros_do_stephen_king():
    livros = {
                "Salem's Lot": "rosa",
                "IT - a Coisa": "cinza",
                "Joyland": "branco",
                "Carrie a estranha": "roxo",
                "Misery": "cinza",
                "The Bachman Books": "marrom",
                "Novembro de 63": "rosa"
            }
    cores = {
                "rosa": 15.0,
                "cinza": 25.0,
                "branco": 35.0,
                "roxo": 200.0,
                "marrom": 1000.0
            }
    for titulo in livros:
        esperado = cores[livros[titulo]]
        obtido = verifica_preco(titulo, livros, cores)
        msg = f'Para o seguinte o livro {titulo}, era esperado {esperado} mas foi obtido {obtido}.\nO dicionário de cores utilizado foi {cores} e o de preços foi {livros}.'
        assert esperado == obtido, msg
