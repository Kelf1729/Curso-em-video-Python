"""Refazer e desafio 35 com as condições
adicionais de classificar o triângulo"""


number1 = float(input('Digite um dos lados:  '))
number2 = float(input('Digite um dos lados:  '))
number3 = float(input('Digite um dos lados:  '))

if number1 == number2 and number1 == number3:
    print('O triângulo apresentado é equilátero\n'
          '{} {} {} '.format(number1, number2, number3))
elif number1 == number2 or number1 == number3:
    print('O triângulo apresentado é isósceles\n'
          '{} {} {} '.format(number1, number2, number3))
elif number1 != number2 and number1 != number3:
    print('O triângulo apresentado é escaleno\n'
          '{} {} {} '.format(number1, number2, number3))