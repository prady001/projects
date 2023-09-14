import json

# Lê o arquivo 'estoque.json'
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

# Cria um dicionário a partir das informações do texto
dicionario = json.loads(texto)

# Inicia a varável que conterá o valor total das compras
total = 0

# Inicia um loop que percorre os elementos contidos no valor da chave 'produtos'
for e in dicionario['produtos']:
    # Acessa os valores 'quantidade' e 'valor' pertencentes à chave 'e' e soma o produto desses valores na variável 'total'
    total += e['quantidade'] * e['valor']

# Printa o valor total das compras
print(total)
