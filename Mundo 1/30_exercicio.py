"""Mostrar se um número digitado pelo usuário é par ou ímpar"""

number = int(input("Digite um número, inteiro:  "))
if number % 2 == 0:
    print('O número digitado {} é par'.format(number))
else:
    print('O número digitado {} é ímpar'.format(number))