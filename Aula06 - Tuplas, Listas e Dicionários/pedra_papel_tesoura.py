import random

def valida_int(texto, min, max):  #Função que valida inteiro dentro do intervalo
    x = int(input(texto))
    while((x < min) or (x > max)):  #Se o usuário digitar um valor fora do intervalo, fica preso no loop
        x = int(input(texto))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate #Declara as variáveis como globais; Não esquecer destas variáveis
    if jogador1 == 1: #Pedra
        if jogador2 == 1: #Pedra
            empate += 1
        elif jogador2 == 2: #Papel
            v2 += 1 #Incrementa as vitórias do jogador2
        elif jogador2 == 3: #Tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
         if jogador2 == 1: #Pedra
            v1 += 1
         elif jogador2 == 2: #Papel
            empate += 1 #Incrementa o número de empate
         elif jogador2 == 3: #Tesoura
            v2 += 1
    elif jogador1 == 3: #Tesoura
        if jogador2 == 1: #Pedra
            v2 += 1
        elif jogador2 == 2: #Papel
            v1 += 1 #Incrementa o número de empate
        elif jogador2 == 3: #Tesoura
            empate += 1

    resultados = [v1, v2, empate]  #jogador1 é indice[0], jogador2 é índice[1], empate é índice[2]; Somatórios
    return resultados


#Programa principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []  #Lista para todas as jogadas
resultados = []  #Lista para os resultados finais
v1 = 0
v2 = 0
empate = 0
 
while True:  #Laço de repetição que fica jogando até querermos parar
    jogador1 = valida_int('Escolha sua jogada: ',0 , 3) #Mensagem que será passada pro input lá na função e força o usuário a digitar um valor entre 0 e 3
    if not jogador1:  #O jogador1 fez a jogada dele, já pula pro próximo
        break
    jogador2 = random.randint(1,3)  #randint é uma função que gera um número aleatório no intervalo que queremos
    jogadas.append([jogador1, jogador2])  #Adicionando as jogadas dentro da lista, em pares
    resultados = vencedor(jogador1, jogador2) #Define quem é o vencedor passando como parâmetro as duas jogadas que acabaram de ser feitas; Para cada resultado, pegamos a trinca de valores que está dentro de `resultados` na função `def vencedor` para ir acumulando no final

for jogada in jogadas:
    for dado in jogada: #Como tem uma lista dentro de jogadas, vai pegar o dado dentro de jogada
        print(dado, end=' ')  #Imprime todas as jogadas na tela
    print() #Quebra linha depois de mostrar os dados

print(f'Número de vitórias do Jogador 1: {resultados[0]}')
print(f'Número de vitórias do Jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')
