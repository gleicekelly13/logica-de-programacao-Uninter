# Algoritmo que fique recebendo frases ou palavras digitadas pelo usuário; Encerrar o algoritmo qdo a palavra "sair" for digitada

print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar escreva "sair".')
while True:  #Cria propositalmente um loop infinito, pq não faz nenhum teste lógico
    texto = input('')
    print(texto)
    if texto == "sair":
     break  # O break diz qdo parar o laço de repetição
print('Encerrando o programa...')
