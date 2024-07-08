# Condicionais de múltipla escolha(elif)
# Menu com as opções
print('1 - maçã')
print('2 - laranja')
print('3 - banana')

# Leitura dos dados convertendo para inteiro
fruta = int(input('Escolha qual fruta deseja comprar: '))
qtd = int(input('Quantas unidades: '))

if (fruta == 1):
    pagar = qtd * 2.30
    print(f'Você comprou {qtd} unidade de maçã: O total a pagar é: {pagar:.2f}')
elif (fruta == 2):
    pagar = qtd * 3.60
    print(f'Você comprou {qtd} unidade de laranja: O total a pagar é: {pagar:.2f}')
elif (fruta == 3):
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} unidade de maçã: O total a pagar é: {pagar:.2f}')
else:
    print('Fruta inexistente')
