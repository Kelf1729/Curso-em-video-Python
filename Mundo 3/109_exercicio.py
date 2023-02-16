"""Continuação dos problemas 107"""
import moeda

n = float(input('Digite o preço do produto:  '))
print(f'O aumento de 10% do valor é {moeda.aumentar(n,10,True)}')