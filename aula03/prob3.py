kwh = int(input('Qual a quantidade de kWh consumida? '))

print('Tipos de instalação:\nR - Residência\nC - Comércio\nI - Indústria')

tipo_instalacao = input('Qual o tipo de insalação utilizado?(R, I ou C) ')

if (tipo_instalacao == 'R' and kwh <= 500):
 preco = kwh * 0.40
 print (f'Você gastou {kwh}/kwh. Valor a pagar é: {preco:.2f}')
 
elif (tipo_instalacao == 'R' and kwh > 500):
 preco = kwh * 0.65
 print (f'Você gastou {kwh}/kwh. Valor a pagar é: {preco:.2f}')
 
elif (tipo_instalacao == 'C' and kwh <= 1000):
 preco = kwh * 0.55
 print (f'Você gastou {kwh}/kwh. Valor a pagar é: {preco:.2f}')
 
elif (tipo_instalacao == 'C' and kwh > 1000):
 preco = kwh * 0.60
 print (f'Você gastou {kwh}/kwh. Valor a pagar é: {preco:.2f}')
 
elif (tipo_instalacao == 'I'):
 if (kwh <= 5000):
  preco = kwh * 0.55
 else:
  preco = kwh * 0.60
 print (f'Você gastou {kwh}/kwh. Valor a pagar é: {preco:.2f}')
