from random import randint
def apostando_em_dados(num_sor, val_ini, num_rod):
    
    # Loop que vai rodar o numero de vezes que é indicado pelo jogador
    for e in range(1, num_rod + 1):
        n = randint(1, 6) # sorteia um número de 1 a 6
        if n == num_sor: 
            # caso o loop tenha começado agora, o valor atualiza em relação ao valor inicial
            if e == 1:
                val_atu = val_ini * (1 + (1 / 3))
            # caso contrario, o valor atualiza em relação à ultima atualização dele
            else:
                val_atu = val_atu * (1 + (1 / 3))
        else:
            # caso o loop tenha começado agora, o valor atualiza em relação ao valor inicial
            if e == 1:
                val_atu = val_ini * (1 - (1 / 6))
            # caso contrario, o valor atualiza em relação à ultima atualização dele
            else:
                val_atu = val_atu * (1 - (1 / 6))
        
    return val_atu

r = apostando_em_dados(1, 150, 2)
print(r)