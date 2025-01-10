def cadastrar_funcionario(id):  # Função para cadastrar um novo funcionário
   print('-----------------MENU CADASTRAR FUNCIONÁRIO-----------------')
   
   funcionario = {'id do Funcionário': id_global}  # Cria um dicionário para armazenar os dados do funcionário
   print(f'id do Funcionário: {id_global}')
   funcionario['nome'] = input('Por favor, entre com o nome do Funcionario: ')  # Solicita os dados do funcionário ao usuário
   funcionario['setor'] = input('Por favor, entre com o setor do Funcionario: ')
   funcionario['salario'] = float(input('Por favor, entre com o salário do Funcionario: '))
   print('-' * 60)

   lista_funcionarios.append(funcionario.copy())  # Adiciona o funcionário à lista de funcionários

   for funcionario in lista_funcionarios:  # Percorre cada dicionário dentro da lista, cada dicionário representa um funcionário com seus dados
    print()
    for chave, valor in funcionario.items():  #Percorre todos os pares chave-valor no dicionário funcionario
      print(f'{chave}: {valor}')

   
   
def consultar_funcionarios():  # Função para consultar os funcionários cadastrados
   while True:
      ('-' * 60)
      print('-----------------MENU CONSULTAR FUNCIONÁRIO-----------------')
      print('Escolha a opção desejada:')
      print('1 - Consultar todos os Funcionários')
      print('2 - Consultar Funcionário por id')
      print('3 - Consultar Funcionários por setor')
      print('4 - Retornar ao menu')
      try:
       opcao = input('Opção: ')

       match(opcao):  # Verifica a opção escolhida pelo usuário e executa a ação correspondente
          case '1':
             print('-' * 25)
             for funcionario in lista_funcionarios:   
              print()
              for chave, valor in funcionario.items():
               print(f'{chave}: {valor}')
            
              
          case '2':
             id = int(input('Digite o iD do Funcionário: '))  # Consulta funcionário por ID
             print('-' * 35)
             for funcionario in lista_funcionarios:  
                if funcionario['id do Funcionário'] == id:  #verifica se o valor associado à chave 'id do Funcionário' é igual ao id procurado.
                   for chave, valor in funcionario.items():
                    print(f'{chave}: {valor}')
                   break
             else:
                print('Id inválido!')
            
          case '3':
             setor = input('Digite o setor do(s) Funcionário(s): ')   # Consulta funcionários por setor
             print('-' * 35)
             setor_encontrado = False

             for funcionario in lista_funcionarios:
               print()
               if funcionario['setor'] == setor:  #verifica se o valor associado à chave 'setor' é igual ao setor procurado pelo usuário
                 for chave, valor in funcionario.items():
                   print(f'{chave}: {valor}')
                 setor_encontrado = True  #Variável usada para controlar se pelo menos um funcionário foi encontrado no setor especificado

             if not setor_encontrado:
                print('Setor inexistente!')

          case '4':  # Retorna ao menu principal
             return 
         
          case _:
             print('Opção inválida!')
             continue
      except ValueError:  #Será executado caso o usuário digite um caractere ao invés de um número.
        print('Entrada inválida. Por favor, digite um número.')
        
      print()
      print('-' * 20)
      print('-' * 60)
      print()

def remover_funcionario():  # Função para remover um funcionário
   while True:
      id = int(input('Digite o id do funcionário a ser removido: '))
      funcionario_encontrado = False

      for funcionario in lista_funcionarios:  # Procura pelo funcionário na lista
       if funcionario['id do Funcionário'] == id:
         lista_funcionarios.remove(funcionario)  #Remove o funcionário da lista
         print('Funcionário removido com sucesso.')
         funcionario_encontrado = True
         break
       
      if funcionario_encontrado:  #Se o resultado for `True`, o laço while é interrompido com break
       break

      else:  #Se o resultado for `False`, imprime `Id inválido` e o laço while continua
       print('Id inválido!')
      
   print('-' * 60)
   print()


#Programa Principal
print('Bem vindos(as) a empresa da Gleice Kelly Oliveira da Silva')
print('-' * 60)

lista_funcionarios = []  # Inicializa a lista de funcionários e o ID global
id_global = 4884103

while True:  # Loop principal do programa
  print('----------------------MENU PRINCIPAL------------------------')
  print('Escolha a opção desejada:')
  print('1 - Cadastrar Funcionários')
  print('2 - Consultar Funcionário(s)')
  print('3 - Remover Funcionário')
  print('4 - Sair')
  opcao = input('Opção: ')
  print('-' * 60)
  try:
  
   if(opcao == '1'):
      id_global += 1
      cadastrar_funcionario(id_global)
     
   elif(opcao == '2'):
      consultar_funcionarios()

   elif(opcao == '3'):
      remover_funcionario()
     
   elif(opcao == '4'):
      break
    
   else:
       print('Opção inválida!')
       continue
  except ValueError:
    print('Entrada inválida. Por favor, digite um número.')
 
     

#lista_funcionarios.append({'Id do Funcionário': 4884104, 'nome': 'Gleice', 'setor': 'Tecnologia', 'salario': 4000.0})
#lista_funcionarios.append({'Id do Funcionário': 4884105, 'nome': 'Carlos', 'setor': 'RH', 'salario': 3000.0})
#lista_funcionarios.append({'Id do Funcionário': 4884106, 'nome': 'Ana', 'setor': 'Tecnologia', 'salario': 4500.0})

