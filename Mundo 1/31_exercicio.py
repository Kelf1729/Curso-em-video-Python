"""Criar um programa que calcule o preço de uma passagem com as seguines condições
*Passagens de até 200km o preço por km rodado será de R$ 0,50
*Passagens com mais de 200km o preço por km rodado será de R$ 0,45"""

distance = float(input("Digite a distância da viagem:  "))
if distance <= 200:
    print('Para uma viagem de {:.2f} km\n'
          'O preço da passagem será de R$ {:.2f} '.format(distance, distance*0.5))
else:
    print('Para uma viagem de {:.2f}\n'
          'O preço da passagem será de R$ {:.2f}'.format(distance, distance*0.45))