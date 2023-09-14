from math import pi, sin
v = float(input('Digite a velocidade: '))
theta_graus = float(input('Digite o ângulo: '))
theta = (theta_graus * pi) / 180
d = ((v ** 2) * sin(2 * theta)) / 9.8

if d < 98:
    print('Muito perto')
if d > 102:
    print('Muito longe')
if 98 <= d <= 102:
    print('Acertou!')




'''print('lado esquerdo')
print((v ** 2) * sin(2 * theta))
print('lado direito')
print(9.8* 100)


if ((v ** 2) * sin(2 * theta)) == 9.8 * 100:
    print('Acertou!')'''