mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']

print(mochila[0][0])
print(mochila[2][1])

print('--------------------------')

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']  
#Como são duas indexações, serão dois laços
for item in mochila:  #Se refere a cada item da mochila
    for letra in item:  #Usa o item para pegar cada letra dele
        print(letra, end='')   #`end = ''` coloca uma letra ao lado da outra sem dar quebra de linha
    print()  #Quebra linha

#Implementação mais simples
#Pode ser usada para passar palavra por palavra por palavra dentro de um conjunto de palavras e identificar se existe algum padrão

print('-------------------------------')
#Mesmo resultado da anterior, só alterando o laço
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate'] 
for i in range(0, len(mochila), 1):  #Primeiro laço com range indo até o tamanho da mochila
    for j in range(0, len(mochila[i]), 1): #Segunda laço com range indo até o tamanho daquele dado específico dentro da mochila
        print(mochila[i][j], end='')
    print()
