from random import randint

r1= randint(1,20)

x = 0

while x < 5:
    num= int(input('escolha um número de 1 a 20: '))
    if  num <= 20 and num >= 1: 
        if num < r1:
            print('Muito baixo')
        elif num > r1:
            print('Muito alto')
        elif num == r1:
            print(f'Acertou em {x} tentativas')
        else:
            break
        x += 1
if x == 5:
    print('Que pena, você perdeu!')