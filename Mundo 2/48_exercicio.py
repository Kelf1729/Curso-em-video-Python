"""Criar um programa que soma todos os valores ímpares
que são múltiplos de 3 no intervalo de 1 até 500"""

soma = 0
for i in range(1,501):
    if i % 2 != 0 and i % 3 ==0:
        soma = soma + i

print('A soma é {}'.format(soma))