"""Criar um programa que compare dois
valores recebidos pelo usuário"""

number1 = int(input("Digite um valor: "))
number2 = int(input("Digite outro valor: "))

if number1 > number2:
    print('O primeiro valor é maior que o segundo\n'
          '{} > {}'.format(number1, number2))
elif number1 < number2:
    print('O segundo valor é maior que o primeiro\n'
          '{} > {}'.format(number2, number1))
else:
    print('Os valores são iguais\n'
          '{} = {}'.format(number1, number2))