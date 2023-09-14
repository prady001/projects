from random import randint
n1 = randint(1, 20)
c = 1

num = True
while num and c <= 5:
    n2 = float(input('Digite um número de 1 a 20:'))
    
    if n2 < n1 and n2 > 0 and n2 < 21:
        print('Muito baixo')
        c += 1
    if n2 > n1 and n2 > 0 and n2 < 21:
        print('Muito alto')
        c += 1
    if n1 == n2:
        print(f'Acertou em {c} tentativas')
        num = False
        c += 1
    
if c > 5 and n1 != n2: 
    print('Que pena, você perdeu!')


