from primo import eh_primo

def primos_entre(a, b):

    prim = []
 
    for p in range(a, b + 1):      
        
        if eh_primo(p):
            prim.append(p)
    return prim
    
        