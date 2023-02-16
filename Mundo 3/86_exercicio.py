"""Criar um programa para construir uma matriz e gerar alguns resultados com ela
Soma dos números pares
soma dos números da terceira coluna
maior valor da segunda linha"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,2):
    for j in range(0,2):
        matriz[i][j] = int(input(f'Digite o valor na posição {i}{j}: '))
print(matriz)
count_par = count_3col = count_2linha = 0
for i in range(0,2): #valores pares
    for j in range(0,2):
        if matriz[i][j] % 2 ==0:
            count_par += matriz[i][j]
print(count_par)