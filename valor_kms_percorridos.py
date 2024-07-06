km = int(input('Digite a quantidade de Kms percorridos: '))
dias = int(input('Digite quantos dias ficou com o carro: '))
valor_dia_carro = 60
valor_km = 0.15
valor_final_aluguel =  (dias * valor_dia_carro) + (km * valor_km)

# Também poderia colocar o valor do preço direto. Ex: preco = 60 * dias + km * 0.15

print(f'Kms percorridos: {km}: ; Total de dias que permaneceu com o carro: {dias}')
print(f'O valor total a pagar é: {valor_final_aluguel}')
