def classifica_caixa(comprimento, peso):
    w = ((-6.193) * comprimento) + (7.312 * peso) - 110.579
    if w > 0:
        return 'verdura'
    else:
        return 'legume'