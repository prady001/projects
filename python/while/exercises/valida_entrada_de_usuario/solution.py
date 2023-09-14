n = int(input('Digite um número: '))
while n % 2 != 0:
   print('Este número não é par, tente novamente.')
   n = int(input('Digite um número: '))

print(f'Você digitou: {n}, onde {n} é o número par válido.')
