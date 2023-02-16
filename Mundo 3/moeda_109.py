def moeda(n):
    return f'R${n:.2f}'

def aumentar(n,p,show=False):
    if show == True:
        return moeda(n*(1+p/100))
    else:
        return n*(1+p/100)

def diminuir(n,p):
    return n*(1-p/100)

def dobro(n):
    return n*2

def metade(n):
    return n/2
