from random import randint
n = randint(1, 20)
number = int(input('Digite um número entre 1 a 20: '))
if number < n:
    print('Muito baixo')
elif number > n:
    print('Muito alto')
else:
    print('Acertou')
    