print("Bem-vindo(a) a Loja da Gleice Kelly Oliveira da Silva")

valor_do_pedido = float(input('Digite o valor do pedido: '))  # Solicita ao usuário o valor do pedido
quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))  # Solicita ao usuário a quantidade de parcelas desejada

# Verifica a quantidade de parcelas e calcula o valor da parcela e o valor total com base nos juros aplicáveis
if(quantidade_parcelas < 4):  # Até 3 parcelas não tem juros
    valor_parcela = (valor_do_pedido * (1 + 0 / 100)) / quantidade_parcelas
    valor_total_parcelado = valor_parcela * quantidade_parcelas
    print(f'O valor das parcelas é de:R$ {valor_parcela:.2f}')
    print(f'O valor total parcelado é de:R$ {valor_total_parcelado:.2f}')

elif(quantidade_parcelas >= 4 and quantidade_parcelas < 6):
    valor_parcela = (valor_do_pedido * (1 + 4 / 100)) / quantidade_parcelas #Cálculo do valor da parcela com base nos juros
    valor_total_parcelado = valor_parcela * quantidade_parcelas # Cálculo do valor total
    print(f'O valor das parcelas é de:R$ {valor_parcela:.2f}')
    print(f'O valor Total Parcelado é de: R$ {valor_total_parcelado:.2f}')

elif(quantidade_parcelas >= 6 and quantidade_parcelas < 9):
    valor_parcela = (valor_do_pedido * (1 + 8 / 100)) / quantidade_parcelas
    valor_total_parcelado = valor_parcela * quantidade_parcelas
    print(f'O valor das parcelas é de:R$ {valor_parcela:.2f}')
    print(f'O valor total parcelado é de:R$ {valor_total_parcelado:.2f}')

elif(quantidade_parcelas >= 9 and quantidade_parcelas < 13):
    valor_parcela = (valor_do_pedido * (1 + 16 / 100)) / quantidade_parcelas
    valor_total_parcelado = valor_parcela * quantidade_parcelas
    print(f'O valor das parcelas é de:R$ {valor_parcela:.2f}')
    print(f'O valor total parcelado é de:R$ {valor_total_parcelado:.2f}')

else:  # Se a quantidade das parcelas não atender a nenhuma das condições acima, ou seja for maior que 13, o bloco abaixo será executado
    valor_parcela = (valor_do_pedido * (1 + 32 / 100)) / quantidade_parcelas
    valor_total_parcelado = valor_parcela * quantidade_parcelas
    print(f'O valor das parcelas é de:R$ {valor_parcela:.2f}')
    print(f'O valor total parcelado é de:R$ {valor_total_parcelado:.2f}')
