from math import pi
def vai_boiar(P, R, r):
    densidade_boia = (P * (10 ** 3)) / (2 * (pi ** 2) * R * (r ** 2))
    densidade_agua = 0.997 
    if densidade_boia <= densidade_agua:
        return True
    if densidade_boia > densidade_agua:
        return False
    