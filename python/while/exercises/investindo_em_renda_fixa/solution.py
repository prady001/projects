def calcula_investimento(inv_ini, num_mes, ativo):
    k = 1
    if ativo == 'CDB':
        i = 0.0130
        bonus = 0.0120
        while k < num_mes + 1:
            if k == 1: # ao inicio do loop, o montante é calculado a partir do valor inicial
                montante = inv_ini * (1 + i)
                k += 1
            elif k  % 6 == 0: # caso contrario o montante é calculado a partir do valor do montante anterior
                montante = montante * (1 + bonus)
                montante = montante * (1 + i)
                k += 1
            else:
                montante = montante * (1 + i)
                k += 1
                

    if ativo == 'LCI':
        i = 0.0160
        while k < num_mes + 1:
            if k == 1:
                montante = inv_ini * (1 + i)
                k += 1
            else:
                montante = montante * (1 + i)
                k += 1

    if ativo == 'LCA':
        i = 0.0145
        bonus = 0.01
        while k < num_mes + 1:
            if k == 1:
                montante = inv_ini * (1 + i)
                k += 1
            elif k % 4 == 0:
                montante = montante * (1 + bonus)
                montante = montante * (1 + i)
                k += 1
                
            else:
                montante = montante * (1 + i)
                k += 1
    return montante