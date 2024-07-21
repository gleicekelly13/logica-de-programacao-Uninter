games = {
    'nome' : ['Super Mario', 'Zelda Ocarina of Time'],  #Todos os nomes estão dentro de uma lista
    'videogame' : ['Supernintendo', 'Nintendo 64'],  #Todos os videogames estão dentro de uma lista
    'ano' : [1990, 1998]  #Todos os anos estão dentro de uma lista
}

print(games)

print('-------------------------')

games = {'nome': [], 'videogame' : [], 'ano' : []}
for i in range(2):
    nome = input('Qual o nome do jogo? ')
    videogame = input('Para qual videogame ele foi lançado? ')
    ano = input('Qual o ano de lançamento? ')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)
