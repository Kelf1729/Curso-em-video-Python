"""Criar um programa que armazena valores em uma lista completa,
Uma de valores pares e uma de valores ímpares"""
lista = []
lista_par = []
lista_impar = []
escolha = ' '
while True:
    n1 = int(input("Digite um valor:  "))
    lista.append(n1)
    escolha = str(input("Digite se você deseja continuar [N/S]:  "))
    if escolha in 'Nn':
        break
for item in lista:
    if item % 2 ==0:
        lista_par.append(item)
    else:
        lista_impar.append(item)
print(f'A lista completa é {lista}\n'
      f'A lista de valores pares é {lista_par}\n'
      f'A lista de valores ímpares é {lista_impar}')