nome = ''  # String vazia é Falsey

while not nome:  # O not Falsey transforma em (Trusthy/True): É equivalente a `while True:`
    # Encerra o laço qdo nome não estiver vazio
    nome = input('Digite seu nome: ')
valor = int(input('Digite um número qualquer: '))
if valor:  # Equivalente `if valor != 0:`
 print('Você digitou um valor diferente de zero.')
else:
   print('Você digitou zero.')
   
