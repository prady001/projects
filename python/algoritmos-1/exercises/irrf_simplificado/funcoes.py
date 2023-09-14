def calcula_contribuicao_inss(salario_bruto):
    if 0 < salario_bruto <= 1045:
        aliq = 0.075
    elif 1045.01 < salario_bruto <= 2089.6:
        aliq = 0.09
    elif 2089.61 < salario_bruto <= 3134.4:
        aliq = 0.12
    elif 3134.4 < salario_bruto <= 6101.06:
        aliq = 0.14
    elif salario_bruto > 6101.06:
        aliq = 671.12
        return 671.12
    return salario_bruto * aliq
  
def calcula_base_de_calculo(salario_bruto, dependentes):
    base_de_calculo = salario_bruto - calcula_contribuicao_inss(salario_bruto) - (dependentes * 189.59)
    return base_de_calculo

def calcula_irrf(salario_bruto, dependentes):
    base = calcula_base_de_calculo(salario_bruto, dependentes)
    if base <= 1903.98:
        ali = ded = 0
    elif base <= 2826.65:
        ali = 0.075
        ded = 142.8
    elif base <= 3751.05:
        ali = 0.15
        ded = 354.8
    elif base <= 4664.68:
        ali = 0.225
        ded = 636.13
    else:
        ali = 0.275
        ded = 869.36
    irrf = (base * ali) - ded
    return irrf
