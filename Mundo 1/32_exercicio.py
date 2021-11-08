"""Criar um programa para determinar se um ano é bissexto ou não
Condições para um ano ser bissexto """

year = int(input("Digite um ano:  "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano não é bissexto {}'.format(year))