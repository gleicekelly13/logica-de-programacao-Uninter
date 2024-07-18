res = lambda x: x * x
print(res(3))

print('--------------------------')

soma = lambda x, y: x + y
print(soma(5, 3))

print('-------------------------')

# Função lambda que recebe dois valores numéricos como parâmetro.
calc = lambda a , b: (a + 5) * b #Ao primeiro valor sempre soma 5, em seguida, multiplca ambos
print(calc(5, 10))  # Retorna o resultado
