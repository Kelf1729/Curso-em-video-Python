"""Faça um programa que leia uma função chamada contador()
parametros de inicio, fim e passo"""
#resolvido mas na gambiara
def contador(i=0,f=0,p=0):
    i = 0
    f = 10
    p = 1
    print(30*'~')
    print(f'Ccontagem de {i} até {f} de {p} em {p}')
    for i in range(i,f+1,p):
        print(f'{i}', end= ' ')
    print('Fim')
    print(30 * '~')
    #
    i = 10
    f = 0
    p = -2
    print(30 * '~')
    print(f'Ccontagem de {i} até {f} de {p} em {p}')
    for i in range(i, f + 1, p):
        print(f'{i}', end=' ')
    print('Fim')
    print(30 * '~')
    #Escolha
    print('Sua vez de escolher')
    i = int(input('Inicio:  '))
    f = int(input('Final:  '))
    p = int(input('Passo:  '))
    print(30 * '~')
    print(f'Ccontagem de {i} até {f} de {p} em {p}')
    for i in range(i, f + 1, p):
        print(f'{i}', end=' ')
    print('Fim')
    print(30 * '~')

contador()