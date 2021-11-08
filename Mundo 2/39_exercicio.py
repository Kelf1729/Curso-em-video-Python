"""Criar um programa para avaliar alistamento
Condições
* Se ele ainda vai ser alistar, com o tempo que falta
* Se é hora de se alistar
* Se já passou da hora de alistar"""

import datetime
year = int(input("Digite o ano de nascimento:  "))

if datetime.date.today().year - year > 18:
    print('Ele já tem mais de 18 anos, já passou\n'
          'da hora de se alistar, tem {} anos'.format(datetime.date.today().year - year))
elif datetime.date.today().year - year == 18:
    print('Ele tem 18 anos, é hora de se alistar\n'
          'Ele tem {} anos'.format(datetime.date.today().year - year))
elif datetime.date.today().year - year < 18:
    print('Ele ainda vai se alistar, falta {} anos'.format( 18 - (datetime.date.today().year - year)))