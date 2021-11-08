"""Faça um programa que leia um nome e diga:
*Quantas vezes aparece a letra a/A
*Em que posição ele parece pela primeira vez
*Em que posição ele parece pela última vez"""
frase = str(input("Digite a frase:  "))
print('Quantas vezes aparece a letra a/A {}\nEm que posição aparece pela primeira vez {}' .format(frase.upper().count('A'), frase.upper().find('A')))
print('Em que posição aparece a primeira vez a letra a/A {}'.format(frase.upper().rfind('A')))