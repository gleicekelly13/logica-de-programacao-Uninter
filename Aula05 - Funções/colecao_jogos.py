def valida_int(pergunta, min, max): #Validando números inteiros
    x = int(input(pergunta))
    while((x < 0) or (x > max)):  # Enquanto o usuário não digitar um número inteiro positivo, ele ficará preso neste laço
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):  # 1º   Função que verifica se o arquivo existe
   try:  #Tentar abrir o arquivo
      a = open(nomeArquivo, 'rt')  #O 't faz parte da sintaxe  (rt => tenta abrir o arquivo para leitura)
      a.close()  # Sempre que abre o arquivo, tem fechar ele, obrigatória essa prática
   except FileNotFoundError:  #Exceção de arquivo não encontrado
      return False  #Se não der certo(se o arquivo não existir), retorna False
   else:  #Se der certo, retorna True
      return True
      
def criarArquivo(nomeArquivo):  #Função que cria um arquivo
   try:  #Tenta criar o arquivo e já abri-lo para escrita
      a = open(nomeArquivo, 'wt+')  #tenta abrir o arquivo limpo para escrita(criar um arquivo), o '+' serve para atualização
      a.close()  
   except:
      print('Erro na criação do arquivo')
   else:  #Se der certo, retorna True
      print(f'Arquivo {nomeArquivo} criado com sucesso\n')


def cadastrarJogo(nomeArquivo, nome_jogo, nome_videogame):  #2º  Inserir no arquivo
   try:
      a = open(nomeArquivo, 'at')  #Tenta abrir para escrita com o conteúdo que já tem dentro dele
   except:
      print('Erro ao abrir o arquivo')
   else:  #Se der certo, escreve no arquivo
      a.write(f'{nome_jogo}; {nome_videogame}\n')  #Os dados que já vão para dentro do arquivo
# `a` é uma variável que recebe algumas informações do arquivo, tem alguns dados de controle do arquivo
   finally:  # Independente do que aconteça, vai precisar fechar o arquivo
      a.close()


def listarArquivo(nomeArquivo):  # 3º  Função que lista o arquivo
   try:
      a = open(nomeArquivo, 'rt')  #Tenta abrir para leitura
   except:
      print('Erro ao ler o arquivo.')
   else:  #Se der certo, vai ler o arquivo 
      print(a.read())
   finally:
      a.close()
      

#programa principal
arquivo = 'games.txt'  #Criação do arquivo
if existeArquivo(arquivo):  # Verificando se o arquivo existe  1º
   print('Arquivo localizado no computador')
else:  #Se o arquivo não existir, vai ser preciso criar o arquivo
   print('Arquivo inexistente.')
   criarArquivo(arquivo)   #Chama a função criarArquivo


while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3) #Força o usuário a escolher um dos itens do menu, se não, fica preso no laço
    if(op == 1):  #Novo item
      print('Opção de cadastrar novo item selecionada...\n')  #2º
      nome_jogo = input('Nome do jogo: ')
      nome_videogame = input('Nome do video game: ')
      cadastrarJogo(arquivo, nome_jogo, nome_videogame)  #Chama a função cadastrarJogo, e passa os parâmetros para ela

    elif(op == 2):  #Listar
      print('Opção de listar selecionada...\n')
      listarArquivo(arquivo)
    elif(op == 3):
        print('Encerrando o programa...')
        break



#manipulação de arquivo normalmente tem tratamento de exceção
#O programa principal consiste em:
#Tentar abrir o arquivo:
#Se o arquivo não existir, ele vai tentar criar o arquivo
#Feito tudo isso, ele cai no menu, onde vai ser possível realizar as opções de cadastrar e listar

# Ordem de criação:
# 1º Verifica se o arquivo existe, se não existe, precisa criar o arquivo
#Depois disso, cai nas opções do menu:
# 2º Cadastrar arquivo
# 3º Listar arquivo
