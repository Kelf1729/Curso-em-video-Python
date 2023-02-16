"""Refazer o problema 107 com uma função chamada
moeda que vai converter os valores na descrição de moeda R$"""
import moeda

n = float(input('Digite o preço do produto:  '))
print(f'O aumento de 10% é {moeda.moeda(moeda.aumentar(n,10))}\n'
      f'O desconto de 20% é {moeda.moeda(moeda.diminuir(n,20))}\n'
      f'O dobro do preço é {moeda.moeda(moeda.dobro(n))}\n'
      f'A metade do valor é {moeda.moeda(moeda.metade(n))}')