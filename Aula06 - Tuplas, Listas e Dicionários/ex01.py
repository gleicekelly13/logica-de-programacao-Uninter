mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')  # Tupla
print(mochila)

print(mochila[0][1]) #Dupla indexação: 0 1° índice é referente a cada item da lista, e o 2° índice é referente a cada caractere da string
print(mochila[0:4])
print(mochila[2:]) #Pega do índice 2 até o final da tupla
print(mochila[-1]) #Inverte a posição e pega o que está por último

print('------------------------')

for item in mochila:
    print(f'Na minha mochila tem {item}')

print('--------------------------------------')

tam = len(mochila)
for i in range(0, tam, 1):
    print(f'Na minha mochila tem: {mochila[i]}')

print('--------------------------')
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete', 'Lanterna')
mochila_grande = mochila + upgrade
print(mochila_grande)
mochila_grande_invertida = upgrade + mochila
print(mochila_grande_invertida)
