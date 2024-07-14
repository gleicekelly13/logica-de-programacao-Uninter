# Algoritmo que calcula a tabuada de todos os números de 1 até 10, e para cada número, calcula a tabuada multiplicado-o pelo intervalo de 1 até 10

tabuada = 1
while(tabuada <= 10):  # Laço que pega os números de 1 a 10
    print(f'TABUADA DE {tabuada}:')
    i = 1 # Varável que efetivamente calcula a tabuada
    while(i <= 10):  # Laço que de fato faz a multiplicação (Calcula as tabuadas)
        print(tabuada * i)
        i += 1
    tabuada += 1 # Incrementa o número que vai calcular a tabuada

print('---------------------------------------')

for tabuada in range(1, 11):  # Laço que pega os números de 1 a 10
    print(f'Tabuada de {tabuada}:')
    for i in range(1, 11): # Laço que de fato faz a multiplicação
        print(tabuada * i)

print('-----------------------------------')

tabuada = 1  # Define o número no quero a tabuada
while(tabuada <= 10):  # Laço que pega os números de 1 a 10
    print(f'TABUADA DE {tabuada}:')
    for i in range(1, 11):  # Laço que de fato faz a multiplicação
        print(tabuada * i)
    tabuada += 1
    

    
