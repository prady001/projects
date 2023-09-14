def esconde_senha(l):
    for e in l:
        senha = l.replace(e, '*')
        l = senha
    return l