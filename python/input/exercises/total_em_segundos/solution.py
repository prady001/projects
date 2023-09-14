dias = int(input('Qual o total de dias? '))
horas = int(input('Qual o total de horas? '))
minutos = int(input('Qual o total de minutos? '))
segundos = int(input('Qual o total de segundos? '))
tot = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print(tot)
5