"""Gerar 5 números aleatorios na tupla mostrando o menor e o maior número da tupla"""
import random

tupla = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
maior = 0
menor = 100
for i in tupla:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f'A tupla é {tupla}\n'
      f'O maior valor é {maior}\n'
      f'O menor valor é {menor}')