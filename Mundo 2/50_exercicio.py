"""Criar um programa que leia 6 números
e some apenas os números pares"""

soma = 0
for i in range(0,6):
    number = int(input('Digite o valor:  '))
    if number % 2 ==0:
        soma += number

print('A soma dos valores pares digitados foi {}'.format(soma))