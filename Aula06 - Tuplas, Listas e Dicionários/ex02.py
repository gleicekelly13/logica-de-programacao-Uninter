mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')  # Tupla
print(f'Tupla: {mochila}')

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']  # Lista
print(f'Lista: {mochila}')

mochila[3] = 'Queijo'
print(mochila)

mochila.append('Ovos')  #Adiciona no final da lista
print(f'Lista: {mochila}')

mochila.insert(1, 'Canivete')  #Insere na posição informada
print(f'Lista: {mochila}')

del mochila[1]  #Deleta do índice informado
print(f'Lista: {mochila}')

mochila.remove('Queijo')  #Deleta o dado informado
print(f'Lista: {mochila}')
