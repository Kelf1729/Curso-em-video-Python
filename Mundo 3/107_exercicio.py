"""Criar um programa com módulos para calcular
aumentar()
diminuir()
dobro()
metade()"""
import moeda

n = float(input('Digite o preço do produto:  '))
print(f'O aumento de 10% é {moeda.aumentar(n,10):.2f}\n'
      f'O desconto de 20% é {moeda.diminuir(n,20):.2f}\n'
      f'O dobro do preço é {moeda.dobro(n):.2f}\n'
      f'A metade do valor é {moeda.metade(n):.2f}')