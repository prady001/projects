from math import sin, asin, pi 
def snell_descartes(n1, n2, theta1):
    theta2 = asin((n1 / n2) * sin(theta1 * (pi / 180)))
    return theta2 * (180 / pi)
    