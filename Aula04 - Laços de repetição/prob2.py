valor = int(input('Digite um valor em R$: '))

while True:
    if(valor >= 100):  # Verifica se o valor é maior ou igual a 100
        cont100 = valor // 100  # Contador para as notas de 100, que só pega a parte inteira da divisão, para saber quantas notas de 100 serão necessárias
        valor = valor - cont100 * 100  # Valor recebe ele mesmo menos o que sobrou da divisão acima, para saber qtas notas ainda faltam
        print(f'Cédulas de 100: {cont100}')
        if not valor:
            break

    if(valor >= 50):
        cont50 = valor // 50  # Contador para as notas de 100, que só pega a parte inteira da divisão, para saber quantas notas de 100 serão necessárias
        valor = valor - cont50 * 50  #Valor recebe ele mesmo menos o que sobrou da divisão acima, para saber qtas notas ainda faltam
        print(f'Cédulas de 20: {cont50}')
        if not valor:
            break
    
    if(valor >= 20):
        cont20 = valor // 20  # Contador para as notas de 100, que só pega a parte inteira da divisão, para saber quantas notas de 100 serão necessárias
        valor = valor - cont20 * 20  #Valor recebe ele mesmo menos o que sobrou da divisão acima, para saber qtas notas ainda faltam
        print(f'Cédulas de 20: {cont20}')
        if not valor:
            break

    if(valor >= 10):
        cont10 = valor // 10  # Contador para as notas de 100, que só pega a parte inteira da divisão, para saber quantas notas de 100 serão necessárias
        valor = valor - cont10 * 10  #Valor recebe ele mesmo menos o que sobrou da divisão acima, para saber qtas notas ainda faltam
        print(f'Cédulas de 10: {cont10}')
        if not valor:
            break

    if(valor >= 5):
        cont5 = valor // 5  # Contador para as notas de 100, que só pega a parte inteira da divisão, para saber quantas notas de 100 serão necessárias
        valor = valor - cont5 * 5  #Valor recebe ele mesmo menos o que sobrou da divisão acima, para saber qtas notas ainda faltam
        print(f'Cédulas de 5: {cont5}')
        if not valor:
            break

    if valor:
        cont1 = valor  # cont1 vai receber o que sobrar
        print(f'Cédulas de 1: {cont1}')
        break

