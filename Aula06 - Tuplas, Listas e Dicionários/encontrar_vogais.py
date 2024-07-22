#Algoritmo que cria uma tupla com 10 palavras. Encontrar dentro desta tupla as vogais de cada palavra. Fazer um print na tela com o nome das palavras e suas respectivas vogais

palavras = ('viagem', 'filme', 'pizza', 'queijo', 'bacon', 'lasanha', 'dormir', 'esportes', 'series', 'musica')
for palavra in palavras:  #Primeiro laço pega a palavra dentro da tupla. É como se dissesse 'Para cada palavra dentro de palavras, faça o print...
    print(f'\nPalavra: {palavra.upper()}. Vogais: ')  #Imprime cada palavra em letras maiúsculas e as vogais que serão exibidas conforme a linha 8
    for letra in palavra:  #Segundo laço pega a letra dentro da palavra 
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')



#Linha 7 => Converte toda a string para minúscula para garantir que não vai pegar uma vogal maiúscula e dar erro e faz um teste de expressão. Lê assim: se a letra minúscula estiver dentro de 'aeiou', executa o print abaixo.
