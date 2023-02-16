"""Criar um programa que escreva
----
mesagem
----"""
def mensagem(frase):
    tam = len(frase) + 6
    print(tam*'~')
    print(f'  {frase}')
    print(tam* '~')

mensagem('olá Mundo')
mensagem('Teste novo')
mensagem('Qualquer frase')