"""Criar uma função~chamada maior(), que recebe vários
parâmetros, e tem que dizer qual o amior deles mostrando todos"""
def maior(*num):
    maior = 0
    for i in num:
        if i > maior:
            maior = i
    print(f'Analisando os valores passados ...')
    for i in num:
        print(i, end= ' ')
    print(f'Foram passados {len(num)} valores e o maior deles é {maior}')

maior(1,2,3,4,5)
maior(2,9,5,7,1)