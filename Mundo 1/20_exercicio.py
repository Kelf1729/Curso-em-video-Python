"Sorteando uma sequência de alunos"
import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))

lista = [n1,n2, n3]
random.shuffle(lista)
print('Sequência de alunos que devem ser escolhida \n {}'.format(lista))
