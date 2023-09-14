from solution import Foguete


foguete = Foguete(100)
distancia = foguete.atualizar(3600)
print(distancia) #Esperado: 100
distancia = foguete.atualizar(3600)
print(distancia) #Esperado: 200 (deve acumular o tempo anterior)