def junta_listas(l):

    i = 0 
    j = 0
    l2 = []
    
    while i < len(l):     
    
        while j  < len(l[i]):
            l2.append(l[i][j])
            j += 1
    
        i += 1
        j = 0
    
    return l2        
    