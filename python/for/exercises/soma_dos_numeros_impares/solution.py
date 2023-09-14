def soma_impares(l):
    
    sum_imp = 0
    for n in l:
    
        if n % 2 != 0:
            sum_imp += n
    
    return sum_imp