"""Escreva um programa para avaliar o empréstimo bancário
Com as seguintes condições

*Valor da casa
*Salário
*Quantos anos para pagar
O valor da prestação não pode ser superior a 30% do salário
"""
house = float(input("Digite o valor da casa: R$ "))
salary = float(input("Digite o salário da pessoa: R$ "))
year = int(input("Digite em quantos anos será o pagamento: "))

installment = house/(year*12)

if installment >= 0.3*salary:
    print('O salário é mais de 30% do valor do salário\n'
          'Salário R$ {:.2f}, valor máximo R$ {:.2f}\n'
          'Valor da prestação R$ {:.2f}\n'
          'Empréstimo NEGADO'.format(salary, 0.3*salary, installment))
else:
    print('O salário é menor de 30% do valor do salário\n'
          'Salário R$ {:.2f}, valor máximo R$ {:.2f}\n'
          'Valor da prestação R$ {:.2f}\n'
          'Empréstimo APROVADO'.format(salary, 0.3 * salary, installment))