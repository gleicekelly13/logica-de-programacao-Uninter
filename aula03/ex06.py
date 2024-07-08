nome = input('Digite um nome: ')
idade = int(input('Digite sua idade: '))

if(nome == 'Gleice'):
    print(f'Olá {nome}')
elif (idade < 18):
    print(f'{nome} tem {idade} anos, é menor de idade!')
elif (idade > 100):
    print(f'{nome} afirma ter {idade} anos, essa pessoa provavelmente não existe')
