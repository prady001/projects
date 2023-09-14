n = 10
maior = 0

def collatz(n):
    count = 0
    while True:
        count += 1
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count
 
while n > 0:
    tamanho = collatz(n)
    if maior < tamanho:
        maior = tamanho
        resp = n
    n -= 1
print(resp)