from solution import Retangulo, Ponto

"""
O retângulo é definido por dois pontos, o superior esquerdo e o inferior direito. No nosso exemplo:

  ^
6_|_     ___. p1
5_|_    |   |
4_|_    |   |
3_|_    |   |
2_|_    .___|
1_|_    p2
  |-|-|-|-|-|->
    1 2 3 4 5 
"""
p1 = Ponto(5, 6)
p2 = Ponto(3, 2)

retangulo = Retangulo(p1, p2)

perimetro = retangulo.calcula_perimetro()
print(perimetro) #Esperado: 12

area = retangulo.calcula_area()
print(area) #Esperado: 8
