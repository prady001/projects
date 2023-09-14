"""def classifica_triangulo(a, b, c):
    if a == b == c:
        return 'equilátero'
    if (a != b) and (a != c) and (b != c) :
        return 'escaleno'
    if (a == b and b !=c) or (a == c and a != b) or (b == c and b != a):
        return 'isósceles'"""
    

def classifica_triangulo(l1, l2, l3):
    if l1 != l2 != l3:
        return 'escaleno'
    if l1 == l2 == l3:
        return 'equilátero'
    else:
        return 'isósceles'