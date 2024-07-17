# Função para validar uma string. Essa função recebe como parâmetroa a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, e caso contrário, retorne falso

def valida_string(texto, min, max):
    s1 = input(texto)  #Colocou uma variável no input para deixar mais dinâmico
    tam = len(s1) #Pega o tamanho da string
    while(tam < min) or (tam > max):  #Valida o tamanho da string, enquanto não passar na verificação, fica preso no laço
        s1 = input(texto)
        tam = len(s1)
    return s1  #Quando conseguir um dado válido, retorna a string, que será utilizada no programa principal

x = valida_string('Digite uma string: ', 10, 30)  #O texto que for digitado aqui, entra como o parâmetro pedido na função
print(f'Você digitou a string: {x}. \nDado válido. Encerrando o programa...', format(x))
