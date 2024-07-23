games = []

game1 = {
    'nome' : 'Super Mario',
    'desenvolvedora' : 'Supernintendo',
    'ano' : 1990
}

game2 = {
    'nome' : 'Zelda Ocarina of Time', 
    'videogame' : 'Nintendo 64',
    'ano' : 1998
}

games = [game1, game2]
print(games)

#Implementação mais dinâmica

game = {}  #dicionario vazio  ;Cada item é um dicionario
games = []  #lista vazia  ;Cada dicionario entra dentro de uma lista

for i in range(2):  #Laço de repetição para ler os dados
 game['nome'] = input('Qual o nome do jogo? ')
 game['videogame'] = input('Para qual videogame ele foi lançado? ')
 game['ano'] = int(input('Qual o ano de lançamento? '))
 games.append(game.copy())  #Copia os dados para dentro da lista
print('-' * 20)
for jogos in games:  #Loop com um laço dentro do outro pq é uma dupla indexação
 for chave, valor in jogos.items():
   print(f'O campo {chave} tem o valor {valor}')
