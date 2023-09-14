

def calcula_aumento(salario):
    
    if salario > 1250:
        aumento = 0.1  
    else:
        aumento = 0.15 
    novo_salario = salario * aumento  
    return novo_salario
'''salario = float(input('Digite seu salário aqui: '))
novo_salario = calcula_aumento(salario)
print(f'O novo salário é: R$ {novo_salario:.2f}')'''
