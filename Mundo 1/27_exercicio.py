"""Fazer um programa que leia o primeiro e último nome de uma pessoa"""
name = str(input("Digite o nome da pessoa:  "))
divisao = name. split()
print('O primeiro nome é {}\nO último nome é {}'.format(divisao[0], divisao[len(divisao) -1]))