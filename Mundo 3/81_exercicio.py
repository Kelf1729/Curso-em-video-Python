"""Criar um programa que recebe vários números com as seguintes condições
Quantos números foram digitados
a lista de valores ordenada de forma descrecente
se o número 5 consta na lista"""
escolha = ' '
count = 0
lista = []
while True:
    n1 = int(input("Digite um valor:  "))
    lista.append(n1)
    count += 1
    escolha = str(input("Você deseja continuar [S/N]:  "))
    if escolha in "Nn":
        break
lista.sort(reverse=True)
print(f"A lista em ordem descrecente {lista}\n"
      f"Com {count} elementos")
if 5 in lista:
    print('Contém o elemento 5')
else:
    print('Não contém o elemento 5 ')