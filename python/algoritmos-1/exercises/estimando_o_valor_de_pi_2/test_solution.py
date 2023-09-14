import pytest
import inspect
import solution


@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado, id=f'n = {entrada}')
    for entrada, esperado in [
        (1, "2"),
        (2, "2\n2"),
        (5, "2\n2\n4\n4\n6"),
        (6, "2\n2\n4\n4\n6\n6"),
        (7, "2\n2\n4\n4\n6\n6\n8"),
        (8, "2\n2\n4\n4\n6\n6\n8\n8"),
    ]
])
@pytest.mark.timeout(5)
def test_sequência_de_numeradores(entrada, esperado, capsys):
    all_functions = inspect.getmembers(solution, inspect.isfunction)
    assert any([f[0] == 'sequencia_dos_numeradores' for f in all_functions]), 'A função sequencia_dos_numeradores não foi definida!'

    solution.sequencia_dos_numeradores(entrada)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'
    assert esperado == stdout, f'Algo de errado! Era esperado fosse impresso:\n{esperado}\nPorém, foi impresso:\n{stdout}.'


@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado, id=f'n = {entrada}')
    for entrada, esperado in [
        (1, "1"),
        (2, "1\n3"),
        (5, "1\n3\n3\n5\n5"),
        (6, "1\n3\n3\n5\n5\n7"),
        (7, "1\n3\n3\n5\n5\n7\n7"),
        (8, "1\n3\n3\n5\n5\n7\n7\n9"),
    ]
])
@pytest.mark.timeout(5)
def test_sequência_de_denominadores(entrada, esperado, capsys):
    all_functions = inspect.getmembers(solution, inspect.isfunction)
    assert any([f[0] == 'sequencia_dos_denominadores' for f in all_functions]), 'A função sequencia_dos_denominadores não foi definida!'

    solution.sequencia_dos_denominadores(entrada)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'
    assert esperado == stdout, f'Algo de errado! Era esperado fosse impresso:\n{esperado}\nPorém, foi impresso:\n{stdout}.'


@pytest.mark.parametrize('entrada, esperado', [
    pytest.param(entrada, esperado, id=f'n = {entrada}')
    for entrada, esperado in [
        (1, "2/1"),
        (2, "2/1\n2/3"),
        (5, "2/1\n2/3\n4/3\n4/5\n6/5"),
        (6, "2/1\n2/3\n4/3\n4/5\n6/5\n6/7"),
        (7, "2/1\n2/3\n4/3\n4/5\n6/5\n6/7\n8/7"),
        (8, "2/1\n2/3\n4/3\n4/5\n6/5\n6/7\n8/7\n8/9"),
    ]
])
@pytest.mark.timeout(5)
def test_sequência_combinada(entrada, esperado, capsys):
    all_functions = inspect.getmembers(solution, inspect.isfunction)
    assert any([f[0] == 'sequencia_combinada' for f in all_functions]), 'A função sequencia_combinada não foi definida!'

    solution.sequencia_combinada(entrada)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'
    assert esperado == stdout, f'Algo de errado! Era esperado fosse impresso:\n{esperado}\nPorém, foi impresso:\n{stdout}.'


@pytest.mark.parametrize('entrada, esperado, anterior, proximo', [
    pytest.param(entrada, esperado, anterior, proximo, id=f'n = {entrada}')
    for entrada, esperado, anterior, proximo in [
        (1, 4.0, 2, 2.6666666666666665),
        (2, 2.6666666666666665, 4.0, 3.5555555555555554),
        (3, 3.5555555555555554, 2.6666666666666665, 2.8444444444444446),
        (4, 2.8444444444444446, 3.5555555555555554, 3.4133333333333336),
        (10, 3.0021759545569062, 3.302393550012597, 3.2751010413348065),
        (100, 3.126078900215409, 3.157339689217563, 3.1570301764551654),
        (1000, 3.140023818600586, 3.143163842419187, 3.1431607055322552),
        (10000, 3.1414355935898644, 3.1417497371492233, 3.1417497057380084)
    ]
])
@pytest.mark.timeout(5)
def test_contruindo_a_função_piwallis(entrada, esperado, anterior, proximo):
    all_functions = inspect.getmembers(solution, inspect.isfunction)
    assert any([f[0] == 'PiWallis' for f in all_functions]), 'A função PiWallis não foi definida!'

    obtido = solution.PiWallis(entrada)
    mensagem = f'Algo deu errado ao testar o valor {entrada}. O esperado era {esperado}, mas foi obtido {obtido}.'
    if obtido == pytest.approx(anterior, abs=1e-12):
        mensagem += ' Será que você não está calculando com um elemento a menos da série?'
    if obtido == pytest.approx(proximo, abs=1e-12):
        mensagem += ' Será que você não está calculando com um elemento a mais da série?'
    if obtido == pytest.approx(esperado/2):
        mensagem += ' Note que o resultado da soma é pi/2, mas queremos o valor de pi.'
    assert obtido == pytest.approx(esperado), mensagem
