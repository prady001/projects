def maior_fator_primo(n):
    l = []    
    i = 1
    while i <= n:
        if n % i == 0 and (0 < i < 10):
            l.append(i)
        i += 1
    return l

r = maior_fator_primo(144)
print(r)
