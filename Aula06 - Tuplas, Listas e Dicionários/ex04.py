#Lista contendo as notas de alunos em uma disciplina, escrever uma expressão para:
#a) Encontrar quantos alunos tiraram nota 7

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))

#b) Alterar a última nota para 4

#notas[-1] = 4
#print(notas)

#c) Encontrar a maior nota
print(max(notas))

#d) Ordenar a lista de notas
notas.sort()
print(notas)

#e) A média das notas
print(sum(notas) / len(notas))
