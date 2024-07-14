# O intervalo é especificado pelo usuário
inicial = int(input('Qual valor desejar iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? ')) 

x = inicial
while (x <= final):
 if (x % 2 == 0):  # Verifica se o número é par
  print(x)
 x = x + 1  #Precisa estar dentro do while, caso contrário, fica preso num loop infinito
