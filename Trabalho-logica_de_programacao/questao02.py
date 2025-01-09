print('-------Bem vindos(as) a loja de Marmitas da Gleice Kelly Oliveira da Silva---------')
print('--------------------------Cardápio-------------------------------')
print('-----------------------------------------------------------------')
print('---|  Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---')
print('---|     P     |       R$ 16.00       |       R$ 15.00       |---')
print('---|     M     |       R$ 18.00       |       R$ 17.00       |---')
print('---|     G     |       R$ 22.00       |       R$ 21.00       |---')
print('-----------------------------------------------------------------')

total = 0  # Variável acumuladora iniciando em zero

while True:  #Criando propositalmente um loop infinito para ler os pedidos e calcular os valores
    sabor = input('Digite o sabor desejado (BA/FF): ')
    if (sabor != 'BA' and sabor != 'FF'):  #Verifica se o usuário digitou os sabores disponíveis
        print('Sabor inválido. Tente novamente\n')
        continue  #Caso o usuário digite um valor diferente dos que estão no cardápio, o laço recomeça
    else: #Quando o usuário escolhe o sabor disponível, o laço segue para escolher o tamanho
        tamanho = input('Escolha o tamanho desejado (P/M/G): ') 
        if(tamanho != 'P' and tamanho != 'M' and tamanho != 'G'): #Verifica se o usuário digitou os tamanhos disponíveis
            print('Tamanho inválido. Tente novamente\n')
            continue  #Se o usário digitar um tamanho diferente dos que estão no cardápio, volta para o início do laço
        elif(sabor == 'BA' and tamanho == 'P'):  #Verificação do sabor e tamanho para coincidir com o preço
            nome_sabor = 'Bife Acebolado'  #Definindo o nome do prato por extenso, para ficar mais claro para o usuário
            preco = 16.00
            print(f'Você escolheu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')
            
        elif(sabor == 'BA' and tamanho == 'M'):
            nome_sabor = 'Bife Acebolado'
            preco = 18.00
            print(f'Você escolheu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')
            
        elif(sabor == 'BA' and tamanho == 'G'):
            nome_sabor = 'Bife Acebolado'
            preco = 22.00
            print(f'Você escolheu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')
            
        elif(sabor == 'FF' and tamanho == 'P'):
            nome_sabor = 'Filé de Frango'
            preco = 15.00
            print(f'Você escolheu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')
            
        elif(sabor == 'FF' and tamanho == 'M'):
            nome_sabor = 'Filé de Frango'
            preco = 17.00
            print(f'Você escolheu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')
            
        elif(sabor == 'FF' and tamanho == 'G'):
            nome_sabor = 'Filé de Frango'
            preco = 21.00
            print(f'Você escolheu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')

        total += preco  #Variável acumuladora somando os valores dos pedidos

        add_pedido = input('\nDeseja mais alguma coisa? (S/N): ')  # Caso o usário deseje adicionar mais pedidos, serão armazenados nesta variável
        if(add_pedido == 'S'):
            continue
        else:
            break  #Se o usuário não desejar pedir mais nada, o laço é encerrado


print(f'\nO valor total a ser pago: R$ {total:.2f}')

        
            

        


    

