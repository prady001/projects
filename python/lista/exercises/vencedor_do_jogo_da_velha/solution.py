def verifica_jogo_da_velha(l):
    i = j = 0
    while j < 3:
        if l[1][j] == l[1][j+1] == l[1][j+2] == 'X':
            j += 1
            return 'X'
    