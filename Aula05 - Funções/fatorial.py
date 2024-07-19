
def valida_int(pergunta, min, max): #Validando números inteiros
    x = int(input(pergunta))
    while((x < 0) or (x > max)):  # Enquanto o usuário não digitar um número inteiro positivo, ele ficará preso neste laço
        x = int(input(pergunta))
    return x

def fatorial(num): #O parâmetro recebe um número do qual vai ser calculado a fatorial dele, e depois vai ser retornado o resultado

    """
    
    Função que calcula a fatorial de um número inteiro
    :param num:
    : return:
    """

    fat = 1 # A fatorial inicial em 1, pq 1 é o valor mínimo para calcular a fatorial
    if num == 0: # Se a fatorial for a fatorial de 0...
        return fat # Retorna 1
    # A partir daqui, só executa caso num > 0
    for i in range(1, num + 1, 1): #Valor inicial da iteração, e o número que queremos + 1, pq o padrão do for é subtrair a posicial final, então para ir até o número que queremos precisa adicionar mais 1
        fat *= i # fat recebe ela mesma multiplicada pela variável i, vai acumulando 
    return fat  #retorna o valor

x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print(f'{x}! = {fatorial(x)}')  #Lê assim: O resultado da fatorial de x é igual ao que for retornado da função fatorial. O x é passado como parâmetro para a função fatorial na variável `num`
    


#Temos 2 variáveis locais:
#num: recebe os dados via parâmetro
#fat: só existe no corpo da função
# as variáveis num e x poderiam ter o msmo nome
#Fatorial de 0 == 1; fatorial de 1 == 1: e os demais números vão regredindo sucessivamente: 2! == 2 * 1
