# Algoritmo que realiza um login em um sistema; O usuário deve informar seu nome e senha

while True:
    nome = input('Qual o seu nome? ')
    if (nome != 'Lenhadorzinho'):
        continue  # Se não cumprir a condição, volta para o início do laço
    
    senha = input('Qual a sua senha? ')
    if (senha == "Uninter"):
        break # Se cumprir a condição, encerra o laço: Se não cumprir a condição, volta para o início do laço
print("Acesso concedido")
