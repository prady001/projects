c = 0 
p1 = input("Já assistiu todos os filmes?")
if p1 == 'sim':
    c = c + 1
p2 = input("Tem camiseta temática?")
if p2 == 'sim':
    c = c + 1
p3 = input("Já se fantasiou de algum personagem?")
if p3 == 'sim':
    c = c + 1
p4 = input("Tem algum action figure/nave/etc?")
if p4 == 'sim':
    c = c + 1
p5 = input("Já foi no Galaxy's Edge, o parque temático da franquia?")
if p5 == 'sim':
    c = c + 1

if c == 2:
    print('Padawan')
elif c == 3 or c == 4:
    print('Jedi')
elif c == 5:
    print('One with the Force')
else:
    print('Inocente')