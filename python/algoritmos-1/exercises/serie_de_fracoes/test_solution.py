import pytest
from pathlib import Path
try:
    from solution import calcula_serie
except ImportError:
    calcula_serie = None


PWD = Path(__file__).parent
program = PWD / "solution.py"

with open(program) as f:
    prog_contents = f.read()

@pytest.mark.skipif(
    calcula_serie and calcula_serie(1, 1, 1) != None or "*" in prog_contents, reason="Está utilizando o operador de * referente ao próximo exercício."
)
@pytest.mark.parametrize('n, esperado',
    [
        pytest.param(n, esperado, id=f'n = {n}')
            for n, esperado in [
                (1, '0'),
                (4, '0\n1\n2\n3'),
                (9, '0\n1\n2\n3\n4\n5\n6\n7\n8'),
            ]
])
@pytest.mark.timeout(5)
def test_imprime_contagem(n, esperado, capsys):
    calcula_serie(1, 1, n)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'
    assert esperado == stdout, f'Algo de errado! Era esperado que fosse impresso:\n{esperado}\nPorém, foi impresso:\n{stdout}.'


@pytest.mark.skipif(
    calcula_serie and calcula_serie(1, 1, 1) != None, reason="Já está no próximo exercício."
)
@pytest.mark.timeout(5)
def test_imprime_valores_calculados(capsys):
    a, b, n = 3, 4, 5
    valores_esperados = [2.3230573125418773e-08, 1.8816764231589208e-06, 0.00015241579027587258, 0.012345679012345678, 1.0]
    calcula_serie(a, b, n)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'

    try:
        obtidos = sorted([float(valor) for valor in stdout.split()])
    except ValueError:
        raise AssertionError('Para este exercício, imprima somente os valores calculados e nada mais.')

    esperado = "\n".join([str(valor) for valor in valores_esperados])
    msg = f'Algo deu errado! Era esperado que fosse impresso: {esperado}\nPorém, foi impresso:\n{stdout}'
    assert len(obtidos) == 5, msg

    for i in range(5):
        assert obtidos[i] == pytest.approx(valores_esperados[i]), msg


@pytest.mark.parametrize('a, b, n, esperado',
    [
        pytest.param(a, b, n, esperado, id=f'a = {a}, b = {b}, n = {n}')
            for a, b, n, esperado in [
                (1, 2, 3, 3.0),
                (2, 3, 4, 1.142578125),
                (3, 4, 5, 1.0124999997096178),
            ]
])
@pytest.mark.timeout(5)
def test_finalizando_série_de_frações(a, b, n, esperado, capsys):
    obtido = calcula_serie(a, b, n)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) == 0, 'Para este exercício não é necessário imprimir nenhuma informação.'
    assert obtido == pytest.approx(esperado), f'Algo deu errado para o calculo da série de frações para os valores a = {a}, b = {b} e n = {n}.\nEra esperado {esperado} mas foi obtido {obtido}.'
