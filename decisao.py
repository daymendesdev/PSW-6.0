notas = []

while True:
    nota_aluno = int(input('Digite a nota do aluno ou -1 para sair:'))
    if nota_aluno == -1:
        break
    notas.append(nota_aluno)
    
print(notas)