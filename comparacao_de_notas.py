nome = input('Nome do Aluno: ')
prova1 = int(input('Digite a nota da 1ª prova: '))
prova2 = int(input('Digite a nota da 2ª prova: '))
media_do_aluno = (prova1 + prova2) / 2

if media_do_aluno >= 6:
    print(f'Parabéns, {nome}, você foi aprovado! ')
    print(media_do_aluno)
elif media_do_aluno >= 4:
    print('Você ficou de recuperação')
    print(media_do_aluno)
else:
    print(f'sinto muito, {nome}, você ficou reprovada')
    print(media_do_aluno)