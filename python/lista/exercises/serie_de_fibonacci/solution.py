def calcula_fibonacci(n):
    
    n1 = 1
    n2 = 1
    c = 0
    l = [1, 1]

    if n <= 0:
        return False
    
    elif n == 1:
        return [1]
    
    else:
        while c < n - 2:
            nth = n1 + n2
            l.append(nth)
            n1 = n2
            n2 = nth
            c += 1
    
    return l