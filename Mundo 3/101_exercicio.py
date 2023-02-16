"""Criar um programa chamado voto para receber a idade da pessoa
e dizer se ela vai poder votar ou não"""
def voto():
    ano_atual = 2023 #problemas com a biblioteca de importação de data today
    idade = int(input('Em que ano você nasceu:  '))
    if ano_atual - idade < 18:
        print(f'A pessoa com {ano_atual - idade} anos não pode votar')
    else:
        print(f'A pessoa com {ano_atual - idade} anos pode votar')

voto()