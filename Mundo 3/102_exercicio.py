"""Criar uma função para gerar um fatorial com documentação incluída"""
def fatorial(n=0, show=False):
    """
    :param n: valor do fatorial
    :param show: mostrar a conta sendo feita
    :return: valor do fatorial
    """
    f = 1
    for i in range(1,n+1):
        f *= i
        if show:
            if i != n:
                print(f'{i} X ',end= ' ')
            else:
                print(f'{i} = ', end=' ')
    return f

print(fatorial(5,show=True))
help(fatorial)