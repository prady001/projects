from math import *
def reflexao_total_interna(n1, n2, a2):
    if sin(a2 * (pi / 180)) > (n1 / n2):
        return True
    else:
        return False
     