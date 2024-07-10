lado1 = int(input('Digite um valor de um lado do triângulo: '))
lado2 = int(input('Digite um valor de um lado do triângulo: '))
lado3 = int(input('Digite um valor de um lado do triângulo: '))

if((lado1 > 0 and lado2 > 0 and lado3 > 0) and (lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2) ):
 print('É um triângulo')
 if(lado1 != lado2 and lado2 != lado3 and lado1 != lado3):
     print('Triângulo Escaleno') 
 else:
   if(lado1 == lado2 and lado2 == lado3):
    print('Triângulo Equilátero')
   else:
     print('Triângulo Isósceles')
else:
  print('Ao menos um dos lados não serve para formar um triângulo')
