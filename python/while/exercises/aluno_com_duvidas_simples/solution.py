tem_duvidas = True

if tem_duvidas:
    resposta_do_aluno = input('Você está com dúvidas? ')

    if resposta_do_aluno == 'não':
        print('Até a próxima')
        tem_duvidas = False
    else:
        print('Pratique mais')
        