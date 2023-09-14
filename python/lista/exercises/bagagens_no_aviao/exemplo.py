from solution import filtra_bagagens

bagagens =  [[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0],[50.3, 30.2, 30.0], [54.0, 30.2, 22.1]]  #Lista das bagagens (que são listas com os parametros)
altura = 55
largura = 35
profundidade = 25

saida = filtra_bagagens(bagagens, altura, largura, profundidade)
print(saida) # Espera que imprima `2`