import pytest
from pathlib import Path
from solution import raiz_quadrada

PWD = Path(__file__).parent
program = PWD / "solution.py"

with open(program) as f:
    prog_contents = f.read()

@pytest.mark.skipif(
    raiz_quadrada(1) != None or '-' in prog_contents, reason="Está utilizando o operador de subtração referente ao próximo exercício."
)
@pytest.mark.parametrize('n, esperado',
    [
        pytest.param(n, esperado, id=f'n = {n}')
            for n, esperado in [
                (1, '1'),
                (4, '1\n3'),
                (9, '1\n3\n5\n7\n9'),
                (16,'1\n3\n5\n7\n9\n11\n13\n15'),
            ]
])
@pytest.mark.timeout(5)
def test_imprime_números_ímpares(n, esperado, capsys):
    raiz_quadrada(n)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'
    assert esperado == stdout, f'Algo de errado! Era esperado que fosse impresso:\n{esperado}\nPorém, foi impresso:\n{stdout}.'


@pytest.mark.skipif(
    raiz_quadrada(1) != None, reason="Já está no próximo exercício."
)
@pytest.mark.parametrize('n, esperado',
    [
        pytest.param(n, esperado, id=f'n = {n}')
            for n, esperado in [
                (1, '0'),
                (4, '3\n0'),
                (9, '8\n5\n0'),
                (16,'15\n12\n7\n0'),
            ]
])
@pytest.mark.timeout(5)
def test_imprime_resultados_das_subtrações(n, esperado, capsys):
    raiz_quadrada(n)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) > 0, 'Para este exercício era esperado que fosse impresso a sequência pedida pelo enunciado.'
    assert esperado == stdout, f'Algo de errado! Era esperado que fosse impresso:\n{esperado}\nPorém, foi impresso:\n{stdout}.'


@pytest.mark.parametrize('n, esperado',
    [
        pytest.param(n, esperado, id=f'n = {n}')
            for n, esperado in [
                (1, 1),
                (4, 2),
                (9, 3),
                (16, 4),
                (25, 5),
                (36, 6),
                (49, 7),
                (64, 8),
                (81, 9),
                (100, 10)
            ]
])
@pytest.mark.timeout(5)
def test_finalizando_raiz_quadrada_por_subtrações(n, esperado, capsys):

    obtido = raiz_quadrada(n)
    stdout, _ = capsys.readouterr()
    stdout = stdout.strip()

    assert len(stdout) == 0, 'Para este exercício não é necessário imprimir nenhuma informação.'
    assert obtido == esperado, f'Algo deu errado para calcular a raiz quadrada de {n}.\nEra esperado {esperado} mas foi obtido {obtido}.'
