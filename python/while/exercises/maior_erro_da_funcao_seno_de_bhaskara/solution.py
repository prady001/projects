from math import *
x = 0
maior = -inf
while x <= 90:
    sen = (4 * x * (180 - x)) / (40500 - (x * (180 - x)))
    sen_ = sin((x * pi) / 180)
    dif = abs(sen - sen_)
    if dif > maior:
        maior = dif
        k = x
    x += 1
print(k)