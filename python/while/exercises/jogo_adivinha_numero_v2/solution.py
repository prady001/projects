from random import randint
n1 = randint(1, 20)

num = True
while num:
    n2 = float(input('Digite um número de 1 a 20:'))

    if n2 < n1:
        print('Muito baixo')
    if n2 > n1:
        print('Muito alto')
    if n1 == n2:
        print('Acertou')
        num = False
        