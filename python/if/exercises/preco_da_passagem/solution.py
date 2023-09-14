distancia = float(input('Distância desejada: '))
if distancia <= 200:
    resultado = 0.5 * distancia
else:
    resultado = (0.5 * 200) + ((distancia - 200) * 0.45)
print(f'{resultado:.2f}')