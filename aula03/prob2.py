n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')

op = input('Escolha um operador: ')

if (op == '+'):
    calculo = n1 + n2
    print(f'O resultado da adição de {n1} e {n2} é: {calculo}')
elif (op == '-'):
    calculo = n1 - n2
    print(f'O resultado da subtracao de {n1} e {n2} é: {calculo}')
elif (op == '*'):
    calculo = n1 * n2
    print(f'O resultado da multiplicação entre {n1} e {n2} é: {calculo}')
elif (op == '/'):
    calculo = n1 / n2
    print(f'O resultado da divisão entre {n1} e {n2} é: {calculo}')
