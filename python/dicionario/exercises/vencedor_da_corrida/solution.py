from math import inf
from tempo_conclusao import calcula_tempo
nome = True
dicionario = {}

while nome:
    nome = input('Digite o nome: ')
    if nome == 'sair':
        break
    a = int(input('Valor da aceleração: '))
    dicionario[nome] = a

dicionario_tempo = calcula_tempo(dicionario)

menor = inf
vencedor = ''
for i in dicionario_tempo:
    if dicionario_tempo[i] < menor:
        menor = dicionario_tempo[i]
        vencedor = i

print(f'O vencedor é {vencedor} com tempo de conclusão de {menor:.2f} s')
"""for i in dicionario.values():"""


