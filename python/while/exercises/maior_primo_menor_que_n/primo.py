def eh_primo(n):
    
    n1 = 2
    
    if n == 1 or n <= 0:
        return False

    while n1 <= n:
        if n % n1 == 0 and n1 != n:
            return False
        if n1 == n:
            return True
        n1 += 1
        
def primos_entre(a, b):

    prim = []
    
    for p in range(a, b + 1):      
        
        if eh_primo(p):
            prim.append(p)
    return prim
    
        