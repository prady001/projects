n = int(input('Digite um número: '))
soma = 0
termo = 1
while n > 0:
    soma += termo
    termo *= 0.5
    n -= 1
print(soma)
