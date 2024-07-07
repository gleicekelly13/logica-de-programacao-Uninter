# Condicionais aninhadas
# Menu com as opções
print('1 - maçã')
print('2 - laranja')
print('3 - banana')

# Leitura dos dados convertendo para inteiro
fruta = int(input('Escolha qual fruta deseja comprar: '))
qtd = int(input('Quantas unidades: '))

if (fruta == 1): # maçã
    pagar = qtd * 2.30 # Se essa condição for verdadeira, vai calcular a quantidade pelo preço da maçã, e armazena variável pagar
    print(f'Você comprou {qtd} maçãs, o total a pagar é: {pagar}')
else: # Caso a condição anterior for falsa, ele cai nesse bloco de código
    if (fruta == 2):
     pagar = qtd * 3.60
     print(f'Você comprou {qtd} laranjas, o total a pagar é: {pagar}')
    else:
     if(fruta == 3):
      pagar = qtd * 1.85
      print(f'Você comprou {qtd} bananas, o total a pagar é: {pagar}')
     else: # Se nenhuma das condições anteriores forem atendidas, esse último bloco será executado
      print('Fruta inexistente')



