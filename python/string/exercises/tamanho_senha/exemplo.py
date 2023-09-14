from solution import tamanho_minimo


resposta = tamanho_minimo('frase para a função que filtra as palavras', 5)
print(resposta)  # Deve imprimir ['função', 'filtra', 'palavras']

resposta = tamanho_minimo('frase para a função que filtra as palavras', 30)
print(resposta)  # Deve imprimir []
