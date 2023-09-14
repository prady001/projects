with open('macacos_me_mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read().split()

c = 0
for e in conteudo:
    '''print(e.lower())
    if e.lower() == 'banana':
        c += 1'''
    palavra_processada = ''.join(filter(str.isalpha, e)).lower()
    if palavra_processada == 'banana':
        c += 1
print(c)
