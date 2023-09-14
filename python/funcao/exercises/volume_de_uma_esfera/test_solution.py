import pytest
from pytest_devlife import util
try:
    import solution
except:
    solution = None
try:
    if solution:
        from solution import calcula_volume_da_esfera
except:
    pass


def setup():
    util.function_exists_in_module(solution, 'calcula_volume_da_esfera')


gabarito = {0.0: 0.0, 0.5: 0.5235987755982988, 1.0: 4.1887902047863905, 1.5: 14.137166941154067, 2.0: 33.510321638291124, 2.5: 65.44984694978736, 3.0: 113.09733552923254, 3.5: 179.59438003021648, 4.0: 268.082573106329, 4.5: 381.7035074111598, 5.0: 523.5987755982989, 5.5: 696.9099703213358, 6.0: 904.7786842338603, 6.5: 1150.3465099894624, 7.0: 1436.7550402417319, 7.5: 1767.1458676442585, 8.0: 2144.660584850632, 8.5: 2572.440784514442, 9.0: 3053.6280592892786, 9.5: 3591.3640018287315, 10.0: 4188.790204786391, 10.5: 4849.048260815845}
@pytest.mark.parametrize(
    'raio, volume',
    [
        pytest.param(raio, volume, id=f'raio={raio}, volume esperado={volume:.3f}') for raio, volume in gabarito.items()
    ]
)
def test_calcula_volume_a_partir_do_raio(raio, volume):
    resultado_obtido = calcula_volume_da_esfera(raio)
    assert resultado_obtido == pytest.approx(volume), f'Algo deu errado no volume da esfera de raio: {raio}.\nEra esperado {volume}, mas obtido foi {resultado_obtido}'
