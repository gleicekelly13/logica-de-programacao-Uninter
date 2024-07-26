cadastro = {'nome' : [], 'sexo' : [], 'ano' : []}  #Cadastro que recebe palavras-chaves com as listas inicialmente vazias

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N] ')
    if terminar.upper() in 'N': #O N será convertido para maiúsculo, e indicará que o usuário não quer fazer mais nenhum cadastro
        break
    if terminar.upper() not in 'S': #Verifica se o usuário digitou outra coisa sem ser 'S'
        print('Digite S para Sim e N para Não')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?') #Se não for fazer nenhum operação matemática, dá para deixar o ano como string
    cadastro['nome'].append(nome)  #Na palavra-chave `nome` faz um append de nome nela
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)
#NÃO FINALIZADO
