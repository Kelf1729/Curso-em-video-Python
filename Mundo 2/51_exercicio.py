"""Criar um programa que gere os 10 primeiros termos de uma PA
fornecendo o primeiro termo e a razão"""

n1 = int(input('Digite o primeiro termo:  '))
r = int(input("Digite a razão da PA: "))

for i in range(0,10):
    print('{} '.format(n1 + r*i))