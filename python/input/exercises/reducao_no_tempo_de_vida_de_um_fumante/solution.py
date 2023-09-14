cigarros = int(input('Número de cigarros diários: '))
anos = int(input('Número de anos: '))
total = cigarros * anos * 365   # Total de cigarros
tempo = (10 * total) / 1440     # Tempo
print(tempo)