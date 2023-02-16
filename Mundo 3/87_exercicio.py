"""Gerador de números da mega sena"""
import random
n1 = int(input('Digite quantos números você deseja sortear:  '))
sorteio = []
for i in range(0,n1):
    for j in range(0,6):
        sorteio.append(random.randint(0,60))
    print(f'jogo {i+1} número {sorteio}')
    sorteio.clear()