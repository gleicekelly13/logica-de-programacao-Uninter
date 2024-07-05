frase = input('Digite uma frase: ')
print(frase)
tam = len(frase)  # Dá o tamanho da string
frase2 = frase[:int(tam/2)]  # Divide o tamanho da string por 2
print(frase2[-2:])   # O python permite com o sinal de (-) acessar uma string ao contrário, do fim para o início.


