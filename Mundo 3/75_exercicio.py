"""Criar um programa que recebe 4 valores, coloca na tupla e responde as perguntas
Quantos valores 9 foram colocados
Em que posição o valor 3 aparece
quantos valores pares foram digitados"""
a = int(input("Digite um valor:  "))
b = int(input("Digite um valor:  "))
c = int(input("Digite um valor:  "))
d = int(input("Digite um valor:  "))
tupla = (a,b,c,d)
count_9 = count_3 = count_par = 0
for i in tupla:
    if i ==9:
        count_9 += 1
    if i % 2 == 0:
        count_par += 1
print(f"O número de vezes que aparece nove é {count_9}\n"
      f"O número da posição do valor 3 é {tupla.index(3)+1}\n"
      f"O número de pares foi {count_par}")