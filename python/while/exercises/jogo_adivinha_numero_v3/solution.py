from random import randint
n1 = randint(1, 20)
c = 0

num = True
while num:
    n2 = float(input('Digite um número de 1 a 20:'))

    if n2 < n1:
        print('Muito baixo')
        c += 1
    if n2 > n1:
        print('Muito alto')
        c += 1
    if n1 == n2:
        print('Acertou')
        num = False
        c += 1
print(f'Acertou em {c} tentativas')