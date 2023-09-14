# Inicializa uma lista vazia para armazenar as palavras
palavras = []

# Solicita ao usuário que insira palavras até que "fim" seja digitado
while True:
    palavra = input("Digite uma palavra ou 'fim' para encerrar: ")
    
    # Verifica se a palavra é igual a "fim" (sem distinguir maiúsculas de minúsculas)
    if palavra.lower() == "fim":
        break  # Encerra o loop se a palavra for "fim"
    
    # Adiciona a palavra à lista
    palavras.append(palavra)

# Itera sobre as palavras na lista e imprime aquelas que começam com 'a'
for palavra in palavras:
    if palavra.lower()[0] == 'a':
        print(palavra)
