#Algoritmo que calcula média de notas em determinada disciplina; Assumindo que a média final é dada pela média aritmética de cinco notas digitadas

soma = 0   #variável acumuladora
cont = 1   #variável contadora

while(cont <= 5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma = soma + x  #Soma a própria (soma) que começa em 0, e acrescenta o valor da nota(x)
    cont = cont + 1  #Aumenta 1 na quantidade de notas digitadas, é como se ele dissesse "conta mais 1 vez",neste caso, até 5 vezes
media = soma / 5  # Precisa estar fora do laço para calcular apenas 1 vez
print(f'Média final: {media}')
