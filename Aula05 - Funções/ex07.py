#Tratando exceções

i = 0
while True:
    try: #Vai tentar ler a string 
        nome = input('Digite seu nome: ')
        ind = int(input('Digite um índice do seu nome digitado: ')) # E acessar o caractere dentro desse nome digitado
        print(nome[ind]) #Vai tentar fazer o print do caractere naquele índice
        break
    except ValueError:
        print('Oops! Nome inválido. Tente novamente...')
    except IndexError:
        print('Oops Índice inválido. Tente novamente...')
    finally:  # Finalmente... essa instrução sempre será executada, independente das exceções.
        print(f'Tentativa {i}')  #Ele vai contar o número das tentativas
        i += 1
