"""Criar um programa que diga se o nome de uma cidade começa com Santos"""
city = str(input("Digite o nome da cidade:  "))
divisao = city.split()
print('Existe o elemento Santos nesse nome, {}'.format('SANTOS' in divisao[0].upper()))
