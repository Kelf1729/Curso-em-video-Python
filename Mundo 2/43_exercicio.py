"""Criar um programa que calcule o IMC
de uma pessoa com as seguintes condições
* abaixo de 18.5: abaixo do peso
* entre de 18.5 e 25: peso ideal
* entre de 25 e 30: sobrepeso
* entre de 30 e 40: obesidade
* acima de 40: obesidade mórbida"""

weight = float(input("Digite seu peso:  "))
height = float(input("Digite sua altura:  "))

imc = weight/height**2

if imc <= 18.5:
    print('O IMC foi de {:.1f}\n'
          'ABAIXO DO PESO'.format(imc))
elif 18.5 < imc <= 25:
    print('O IMC foi de {:.1f}\n'
          'PESO IDEAL'.format(imc))
elif 25 < imc <= 30:
    print('O IMC foi de {:.1f}\n'
          'SOBREPESO'.format(imc))
elif 30 < imc <= 40:
    print('O IMC foi de {:.1f}\n'
          'OBESIDADE'.format(imc))
elif imc > 40:
    print('O IMC foi de {:.1f}\n'
          'OBESIDADE MÓRBIDA'.format(imc))

