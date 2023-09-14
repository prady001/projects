def classifica_idade(idade):
    if idade <= 11:
        return 'crianca'
    if 12 <= idade <= 17:
        return 'adolescente'
    else:
        return 'adulto'
    