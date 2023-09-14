A = B = C = D = E = F = count = 0
while True:
    n = int(input())
    if n < 0:
        break
    if n <= 11:
        A += 1
    elif n <= 17:
        B += 1
    elif n <= 25:
        C += 1
    elif n <= 35:
        D += 1
    elif n <= 59:
        E += 1
    else:
        F += 1
    
    count += 1

Pa = 100 * (A / count)
Pb = 100 * (B / count)
Pc = 100 * (C / count)
Pd = 100 * (D / count)
Pe = 100 * (E / count)
Pf = 100 * (F / count)

print(f'0-11 anos: {Pa:.2f}%')
print(f'12-17 anos: {Pb:.2f}%')
print(f'18-25 anos: {Pc:.2f}%')
print(f'26-35 anos: {Pd:.2f}%')
print(f'36-59 anos: {Pe:.2f}%')
print(f'Acima de 60 anos: {Pf:.2f}%')
