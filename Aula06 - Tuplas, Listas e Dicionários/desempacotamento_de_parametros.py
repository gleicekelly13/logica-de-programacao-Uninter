def soma(*num):  #O asterisco na frente do parâmetro, indica que a variável será uma tupla de tamanho qualquer
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:  #Passa os dados como parâmetros
        acumulador += i  #Os dados serão iterados sob a tupla e serão somados 
    return acumulador  #E retornados

print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n')   #Esses valores são passados como parâmetros
