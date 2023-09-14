valor = float(input('Valor da casa: '))
salario = float(input('Salário: '))
quantidade_anos = float(input('Quantidade de anos: '))
if valor / (quantidade_anos * 12) <= 0.3 * salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
