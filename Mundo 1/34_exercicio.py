"""Criar um programa que calcule o aumento de salário de um funcionário com as seguinte condições
*Salários acima de/até R$ 1250,00 um aumento de 10%
*Salários abaixo de R$ 1250,00 um aumento de 15%"""

salary = float(input('Digite o salário:  '))

if salary >= 1250:
    print('O salário era de R$ {:.2f} e foi para R$ {:.2f}'.format(salary, salary*1.10))
else:
    print('O salário era de R$ {:.2f} e foi para R$ {:.2f}'.format(salary, salary * 1.15))