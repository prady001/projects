def nivel_idh(idh):
    if (idh >= 0.8) and (idh <= 1000):
        return 'Muito Alto'
    if (idh >= 0.7) and (idh < 0.8):
        return 'Alto'
    if (idh >= 0.555) and (idh < 0.7):
        return 'Médio'
    if (idh >= 0.35) and (idh < 0.555):
        return 'Baixo'
    else:
        return 'Sem dados'