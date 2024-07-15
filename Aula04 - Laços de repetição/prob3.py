total = 0  # Total de pessoas
dinheiro = 0
idades_acumuladas = 0

while True:  # O laço vai ler idades e calcular ingressos
    idade = int(input('Qual a sua idade? '))
    if(idade == 0):
        break

    total += 1  # Acrescente mais uma pessoa
    idades_acumuladas += idade  # Acrescenta mais uma idade
    if(idade < 3):
        ingresso = 0
    else:
        if(idade > 12):
           ingresso = 30 
        else:
            ingresso = 15
    
    dinheiro += ingresso  # Equivalente a `dinheiro = dinheiro + ingresso`

media = idades_acumuladas / total  # Calcula as idades acumuladas divididas pelo total de pessoas

if(total > 0):
 print(f'Total de pessoas: {total}')
 print(f'Total arrecadado: {dinheiro}')
 print(f'Média de idades: {media}')


