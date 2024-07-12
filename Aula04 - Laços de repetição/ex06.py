# Algoritmo que calcula a média dos números pares de 1 ate 100(1 a 100 inclusos) . Utilizando for

soma_pares = 0
cont_pares = 0

for i in range(1, 101): # i representa o número 
 if(i % 2 == 0):  # Verifica se o número é par; Se o número for ímpar, o laço simplesmente passa para a próxima iteração, ignorando qualquer operação de soma ou incremento do contador.
  soma_pares += i # Adiciona o número par à soma
  cont_pares += 1  # Incrementa a contagem de números pares
media = soma_pares / cont_pares  # Tudo que somou dividido por tudo que foi contado
print(f'A média dos números pares de 1 até 100 é: {media}')
