"Sorteando um aluno"
import random
n1 = str(input('Digite o nome:  '))
n2 = str(input('Digite o nome:  '))
n3 = str(input('Digite o nome:  '))
lista = [n1, n2, n3]
print("O aluno escolhido foi, {}".format(random.choice(lista)))

