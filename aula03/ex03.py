# Expressões lógicas e álgebra booleana

m1 = float(input('Digite sua nota final na matéria 1: '))
m2 = float(input('Digite sua nota final na matéria 2: '))
m3 = float(input('Digite sua nota final na matéria 3: '))

if(m1 >= 7 and m2 >= 7 and m3 >= 7):
    print('O aluno está aprovado!')
else:
    print('O aluno está reprovado!')
