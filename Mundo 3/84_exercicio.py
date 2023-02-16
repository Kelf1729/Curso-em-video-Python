"""Criar uma lista única para receber números pares e ímpares"""
lista = [[],[]]
for i in range(0,7):
    n1 = int(input("Digite um valor inteiro:  "))
    if n1 % 2 == 0:
        lista[0].append(n1)
    else:
        lista[1].append(n1)

print(f"Os valores pares são {lista[0]}\n"
      f"Os valores ímpares são {lista[1]}")