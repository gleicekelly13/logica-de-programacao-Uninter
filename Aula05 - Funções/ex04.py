def soma3(x = 0, y = 0, z=0):
    res = x + y + z
    return res

retornado = soma3(1, 2, 3)
print(retornado)

print('---------------------------------------')

print(soma3(2, 2))  #Executa primeiro o que está dentro dos parênteses, e joga no print
print('-------------------------------------')

retornado1 = soma3(1, 2, 3)  
retornado2 = soma3(1, 2)
retornado3 = soma3()
print(f'Somatórios: {retornado1}, {retornado2} e {retornado3}') #Pegou o resultado de cada uma delas e fez só um print mostrando os somatórios
