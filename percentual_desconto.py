preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0 - 100%): '))
desconto = (percentual / 100 * preco)   # Também poderia ser preco * (percentual / 100)
preco_final = preco - desconto

print(f'O valor do produto é {preco}. O percentual de desconto é {percentual}%')
print(f'O valor calculado de desconto é: {desconto}. Então o valor do produto fica {preco_final:.2f}')

