"""Criar um programa que recebe o valor do número em extenso e retorna o valor em tipo número"""
extenso = ('zero','um','dois','três','quadro','cinco')
n1 = int(input("Digite um número entre 0 e 5:  "))
print(f"Você digitou o valor {n1} sendo o extenso dele é, {extenso[n1]}")