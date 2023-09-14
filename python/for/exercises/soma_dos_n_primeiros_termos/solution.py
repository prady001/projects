n = int(input('Digite um número n inteiro: '))
s = 0
k = 0
while k < n:
    e = 1 / (2 ** k)
    s += e
    k += 1
print(s)
