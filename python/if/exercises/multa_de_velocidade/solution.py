velocidade = float(input('Digite sua velocidade: '))
if velocidade <= 80.00:
    print('Não foi multado')
else:
    multa = (velocidade - 80) * 5
    print(f'{multa:.2f}')