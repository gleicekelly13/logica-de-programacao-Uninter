print('1 - Coxinha R$ 5.00')
print('2 - Pastel R$ 7.00')
print('3 - Café R$ 4.00')
print('4 - Suco R$ 6.00')
print('5 - SAIR')

total = 0  # Variável acumuladora
while True:  # Criando um loop infinito até resolver sair
    pedido = int(input('Escolha o produto: '))

    if(pedido == 1):
        qtd = int(input('Quantas unidades deseja? '))
        total = total + qtd * 5.00
    elif(pedido == 2):
        qtd = int(input('Quantas unidades deseja? '))
        total = total + qtd * 7.00
    elif(pedido == 3):
        qtd = int(input('Quantas unidades deseja? '))
        total = total + qtd * 4.00
    elif(pedido == 4):
        qtd = int(input('Quantas unidades deseja? '))
        total = total + qtd * 6.00
    elif(pedido == 5):
        break
    else:
        print('Opção inválida')
print(f'O total a pagar é: R$ {total:.2f}')
        
 
