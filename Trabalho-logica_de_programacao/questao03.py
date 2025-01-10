def escolha_modelo():   #Solicita ao usuário que escolha um modelo de camiseta entre quatro opções 
    while True:
     print('MCS - Manga Curta Simples')
     print('MLS - Manga Longa Simples')
     print('MCE - Manga Curta com Estampa')
     print('MLE - Manga Longa com Estampa')
     modelo = input('Escolha o modelo desejado: ')

     if(modelo == 'MCS'):
         valor_unitario = 1.80  
         return valor_unitario  #Retorno do valor do modelo com base na escolha do usuário
     
     elif(modelo == 'MLS'):
         valor_unitario = 2.10
         return valor_unitario
     
     elif(modelo == 'MCE'):
         valor_unitario = 2.90
         return valor_unitario
     
     elif(modelo == 'MLE'):
         valor_unitario = 3.20
         return valor_unitario
     
     else: #Caso o usuário escolha um modelo diferente dos listados acima, ficará preso no laço até escolher um dos modelos citados
         print('Escolha inválida, entre com o modelo novamente\n')
         continue


def num_camisetas():  #Função para escolher a quantidade de camisetas, e aplica o desconto aproopriado com base na quantidade
    while True:
     try: #Vai tentar executar esse bloco de instruções: Armazena a quantidade de camisetas e dá um desconto de acordo com cada condição
         qtd_camisetas = int(input('\nDigite a quantidade de camisetas: '))
         if(qtd_camisetas > 20000):
             print('Não aceitamos tantas camisetas de uma vez\nPor favor, entre com o número de camisetas novamente\n')
             continue
         
         elif(qtd_camisetas < 20):
             desconto = 0

         elif(qtd_camisetas < 200):
             desconto = 5

         elif(qtd_camisetas < 2000):
             desconto = 7

         else:
             desconto = 12

         valor_com_desconto = qtd_camisetas * (1 - desconto / 100)  #Variável que armazena o cálculo do valor ajustado da quantidade de camisetas após aplicar o desconto percentual
         return valor_com_desconto
     
     except ValueError:  #Trata a exceção no caso do usuário digitar um valor que não seja numérico, exibirá uma mensagem de erro, e só sairá do laço até digitar um valor numérico dentro das condições
         print('Entrada inválida. Por favor, digite um número')
            

def frete():  # Função para escolher o tipo de frete entre 3 opções
    while True:
        print('\n1 - Frete por transportadora - R$ 100.00')
        print('2 - Frete por Sedex - R$ 200.00')
        print('0 - Retirar pedido na fábrica - R$ 0.00')
        try:
         tipo_frete = int(input('Escolha o tipo de frete(1/2/0): '))

         if(tipo_frete == 1):
             return 100.00
         
         elif(tipo_frete == 2):
             return 200.00
         
         elif(tipo_frete == 0):
             return 0.00
         
         else:  #Retorna a mensagem de erro, caso o usuário digite um valor que não está especificado nas condições
             print('Opção inválida, tente novamente.')

        except ValueError:  
            print('Entrada inválida. Por favor, digite um número')


#programa principal
print('Bem vindos(as) a Fabrica de Camisetas da Gleice Kelly Oliveira da Silva\n')
#As variáveis armazenam os valores retornados pelas funções
modelo = escolha_modelo()  #Armazena o valor unitário da camiseta ecolhida pelo usuário e chama a função
qtd_camisetas = num_camisetas()  #Armazena a quantidade de camisetas que o usuário deseja comprar já aplicando o desconto
tipo_frete = frete()  #Armazena o valor do frete escolhido

try: #Tenta executar que está dentro do bloco
 total = (modelo * qtd_camisetas) + tipo_frete   #Calcula o total
 print(f'\nDescrição do pedido - valor do modelo: {modelo:.2f}; quantidade de camisetas com desconto: {qtd_camisetas:.2f}; valor do frete: {tipo_frete:.2f}')  #Imprime a descrição do pedido e o valor total
 print(f'Valor total: {total:.2f}')

except Exception as e:  #Caso haja alguma exceção durante a execução do bloco `try`, será capturada neste bloco `except`
 print(f'Ocorreu um erro ao calcular o valor total: {e}')
