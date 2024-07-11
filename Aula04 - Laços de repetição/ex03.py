# Validando entrada com um loop
# Algoritmo que recebe um valor do tipo inteiro via teclado; 
# O programa só aceita valores inteiros e positivos, obrigatoriamente
# Qualquer valor negativo ou igual a zero deve ser rejeitado pelo programa e um novo valor deve ser solicitado

x = int(input('Digite um valor maior do que zero: '))
while(x <= 0):
    x = int(input('Digite um valor maior do que zero: '))  #Enquanto não digitar um valor maior que zero, fica preso no loop
print(f'Condição atendida! Você digitou {x}, que é um valor maior que zero')
