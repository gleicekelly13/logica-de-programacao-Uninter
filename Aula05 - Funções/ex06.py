# Tratando exceções
while True:
    try: #Pede para o programa tentar executar esse código
        x = int(input('Por favor, digite um número: '))
        print(x)
        break # Se o usuário digitar o número, o laço é encerrado
    #Exceção
    except ValueError: #Se o usuário não digitar um número inteiro, ele manda uma mensagem de erro. Trata o erro específico
        print('Oops! Número inválido. Tente novamente...')


