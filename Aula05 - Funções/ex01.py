def realce ():
    print('|','-' * 10,'|')
    print('|','-' * 10,'|')

realce()  #Chama a função para ser executada
print('     MENU   ')   #EXibe a string
realce()  #Chama a função novamente para ser executada

#Função com parâmetro
def realce (s1):
    print('|','-' * 10,'|')
    print('|','-' * 10,'|')
    print(s1)
    print('|','-' * 10,'|')
    print('|','-' * 10,'|')

realce(' Hello World!   ')
