""""""
lista = []
maior = 0
menor = 10**100
for i in range(0,4):
    n1 = int(input("Digite um valor:  "))
    lista.append(n1)
    if maior < n1:
        maior = n1
    if menor > n1:
        menor = n1
print(f"o maior valor é {maior}\n"
      f"O menor valor foi {menor}\n"
      f"A lista foi {lista}")
print('Posição dos maiores valores')
for pos,item in enumerate(lista):
    if item == maior:
        print(f"Posição {pos+1}", end= '...')
print('\nPosição dos menores valores')
for pos,item in enumerate(lista):
    if item == menor:
        print(f"Posição {pos+1}", end= '...')
