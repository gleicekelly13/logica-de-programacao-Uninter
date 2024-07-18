# Tratamento de exceções

def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Erro de divisão por zero...')
    except:  # É como se contemplasse todas as outras exceções que não foram listadas
        print('Algo de errado aconteceu...')
    else:
        return res # Se o `try` conseguir executar o bloco, vai cair no else e retornará o res
    finally:
        print('Executará sempre!')

print(div())
