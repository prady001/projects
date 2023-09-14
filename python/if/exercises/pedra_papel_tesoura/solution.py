def pedra_papel_tesoura(p1, p2):
    opcoes_validas = ['pedra', 'papel', 'tesoura']

    if (p1 not in opcoes_validas) or (p2 not in opcoes_validas):
        return 'Escolha pedra, papel ou tesoura para jogar'
    
    if p1 ==  p2:
        return 'empate'
    elif (p1 == 'pedra' and p2 == 'tesoura') or \
         (p1 == 'tesoura' and p2 == 'papel') or \
         (p1 ==  'papel' and p2 == 'pedra'):
        return 'um'
    else:
        return 'dois'



"""# Recebe os inputs dos jogadores

def pedra_papel_tesoura(p1, p2):
    p1 = input('pedra, papel ou tesoura?')
    p2 = input('pedra, papel ou tesoura?')
    if p1 == p2:
        return 'empate'"""