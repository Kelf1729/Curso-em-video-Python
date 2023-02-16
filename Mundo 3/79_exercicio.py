"""Criar um programa que recebe valores de uma lista, coloque eles em uma lista e não receba
valores duplicados"""
lista = []
escolha = ' '
while True:
    n1 = int(input("Digite um valor:  "))
    if n1 not in lista:
        lista.append(n1)
    else:
        print("Valor duplicado, escolha outro valor:  ")
    escolha = str(input("Deseja continuar[N/S]:  ")).upper()
    if escolha == "N":
        break
print(lista)
