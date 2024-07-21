mochila = {'Laptop' : 1, 'Smartphone' : 2, 'Power Bank' : 3, 'Carregadores e Cabos' : 4}  #Criação do Dicionário
print(f'Mochila: {mochila}')

print('-------------------------------------')

game = {
    'nome' : 'Super Mario',  #palavra-chave : dado
    'desenvolvedora' : 'Nintendo',
    'ano' : 1990
}

print(game)
print(game['nome'])  #Acessa o dado pela palavra-chave
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())  #Imprime só os dados e ignora as palavras-chaves

print('-----------------------')

for values in game.values():
    print(values)

print('------------------------------')

print(game.keys()) #Imprime só as chaves

for keys in game.keys():
    print(keys)

print('---------------------------')

print(game.items())

for keys, values in game.items():  #Itera em ambos, na hora de fazer o loop coloca duas variáveis
    print(f'{keys} : {values}')
