def borda(s1): # Recebe como parâmetro um texto
    tam = len(s1) #Pega o tamanho da string
    if tam:  # Só imprime caso exista algum caractere
        print('+','-' * tam,'+')  #Print da linha de cima
        print('|', s1, '|')  #Print da string adaptada
        print('+','-' * tam,'+')  #Print da linha de baixo; Faz o prints adaptados: pega o tamanho da string e multiplica pela quantidade de tracinhos, para ter certeza que vai dar bem no tamanho desejado

borda('Hello World!')
borda('Lógica de programação')
