"""Criar um programa que receba valores, ordene eles e depois diga a posição do valor adicionado"""
lista = []
for i in range(0,5):
    n1 = int(input("Digite um valor:  "))
    lista.append(n1)
    lista.sort()
    if len(lista)-1 == lista.index(n1):
        print(f"O valor {n1}, foi adicionado no final da lista")
    else:
        print(f'Valor {n1}, adicionado na posição {lista.index(n1)}')
print(lista)