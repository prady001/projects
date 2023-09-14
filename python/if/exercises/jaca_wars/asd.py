def aluno_aprovado(nota):
    if nota >= 5:
        return True
    else:
        return False
nota = 10
if aluno_aprovado(nota):
    print('Você foi aprovado na disciplina.')
else:
    print('Você não foi aprovado na disciplina.')
    