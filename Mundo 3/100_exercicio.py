"""Criar duas funções uma para gerar 5 números sorteados
e a outra para somar os valores sorteados pares"""
def sortear(): #Primeira função
    import random
    lista = []
    for i in range(0,5):
        lista.append(random.randint(1,100))
    def somarpar(lista): #Segunda função 
        soma = 0
        for i in lista:
            if i % 2 == 0:
                soma += i
        print(f'Os valores foram {lista} e a soma dos pares é {soma}')
    somarpar(lista)

sortear()

