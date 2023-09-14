from math import *
def calcula_tempo(di):
    dic1 = {}
    for e in di:
        a = di[e]
        t = sqrt((2 * 100) / a)
        dic1[e] = t
    return dic1

     