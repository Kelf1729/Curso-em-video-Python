"""Criar um programa que diga se existe o nome Silva no nome da pessoa"""
name = str(input("Digite o nome da pessoa:  "))
print('Existe o elemento Silva nesse nome, {}'.format('SILVA' in name.upper()))