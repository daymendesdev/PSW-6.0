nome = input('Nome:')
idade = int(input('Idade'))

while idade <= 17:
    print('Verifique sua idade e tente novamente')
    idade +=18
    idade = int(input('Digite sua idade'))
    print('Cadastro realizado com sucesso')
     