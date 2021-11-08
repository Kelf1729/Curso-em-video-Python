"""Criar um programa que leia 3 números e defina qual é o maior e menor deles"""

n1 = int(input('Digite um número: '))
maior = menor = n1
if n1 > maior:
    maior = n1
if n1 < menor:
    menor = n1

n2 = int(input('Digite um número: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
    
n3 = int(input('Digite um número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print('O maior é {}\n'
      'O menor é {}'.format(maior,menor))
