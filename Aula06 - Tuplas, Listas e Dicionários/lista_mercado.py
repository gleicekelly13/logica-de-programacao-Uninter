item = []  #Lista vazia    list() -> Também é uma forma de criar lista vazia
mercado = []

for i in range(3):  #Um laço que vai até 3, para cadastrar 3 itens
    item.append(input('Digite o nome do item: '))  #Um appende para colocar cada item na lista 
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])  #Copia a lista `item` e faz um append dela para dentro da lista do mercado
    item.clear()  #Limpa a lista de itens para cadastrar o próximo, se não fizer isso, ele fica sempre adicionando e não limpa a variável, fica repetindo o item que já foi colocado
print(mercado)

print('----------------------')
#Exercício anterior resolvido de forma mais simples

mercado = []  #Cria uma lista vazia

for i in range(3): #Um laço que vai até 3, para cadastrar 3 itens
    nome = input('Digite o nome do item: ')  #Lê os 3 valores separadamente
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])  #Faz só um append com os 3 itens direto do formato de uma lista
print(mercado)

print('-----------------------------------')
#Cálculo do valor a ser pago

soma = 0
print('Lista de compras:')
print('-' * 20)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')
