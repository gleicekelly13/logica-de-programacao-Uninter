lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original  #A lista_referenciada é como um apontador para a lista_original, só recebe o endereço dela...
print(lista_original)
print(lista_referenciada)

print('--------------------')

lista_referenciada[0] = 2  #Por isso, qdo altera uma lista, altera a outra tbm
print(lista_original)
print(lista_referenciada)


#Cópia
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:]  #O `[:]` significa que está pegando toda a lista, mas poderia fatiá-la se quisesse
print(lista_original)
print(lista_referenciada)

print('--------------------------------')
lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)
