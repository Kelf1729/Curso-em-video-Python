"""Faca um programa que leia um número no intervalo de 0 até 9999
Depois exiba a posição de cada número"""
number = int(input('Digite um número:  '))
m = number // 1000 % 10
c = number // 100 % 10
d = number // 10 % 10
u = number // 1 % 10
print('Unidade {}\ndezena {}\ncentena {}\nmilhar {} '.format(u, d, c, m))
