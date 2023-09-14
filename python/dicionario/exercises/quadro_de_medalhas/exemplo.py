from solution import pais_campeao


entrada = {
    'México': {
        'ouro': 0,
        'prata': 3,
        'bronze': 2
    },
    'Malásia': {
        'ouro': 0,
        'prata': 4,
        'bronze': 1
    },
    'Suriname': {
        'ouro': 2,
        'prata': 0,
        'bronze': 1
    }}

resposta = pais_campeao(entrada)
print(resposta) # Deve imprimir 'Suriname'
