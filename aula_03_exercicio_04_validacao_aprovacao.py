# Exercicio 4 (3) : Sistema de Validação de Aprovação Acadêmica Multidisciplinar
m1 = float(input('Digite a nota 1ª matéria: '))
m2 = float(input('Digite a nota 2ª matéria: '))
m3 = float(input('Digite a nota 3ª matéria: '))
if m1 >= m2 >= m3 >= 7:
    print('O aluno está aprovado de ano! ')
else:
    print('O aluno não passou de ano! ')