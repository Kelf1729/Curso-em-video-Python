"""Criar um programa que recebe nomes e pesos e diga quais as pessoas mais pesadas e mais leves"""
maior = 0
menor = 10**100
escolha = ' '
dados = []
lista = []
while True:
    nome = str(input("Digite o nome da pessoa:  "))
    peso = float(input("Digite o peso da pessoa:  "))
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso
    dados.clear()
    escolha = str(input('Deseja continuar [N/S]:  '))
    if escolha in "Nn":
        break
print(f"O maior peso foi {maior}")
print("Os nomes com maior peso são")
for p in lista:
    if p[1] == maior:
        print(f"{p[0]}", end= '...')

print(f"\nO menor peso foi {menor}")
print("os nomes com menor peso foram")
for p in lista:
    if p[1] == menor:
        print(f"{p[0]}", end= '...')