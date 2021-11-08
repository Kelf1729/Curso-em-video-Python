"""Criar um programa que leia o nome de um usuário
* mostrar todas as letras em maiúsculas
* O nome com todas as letras em minúsculas
* Quantas letras existem sem considerar os espaços
* Quantas letras tem o primeiro nome"""

name = str(input("Digite o nome do usuário:  "))
print('Todas as letras em maiúscula\n {}'.format(name.upper()))
print('Todas as letras em minúsculas\n {}'.format(name.lower()))
print('Tamanho do string sem considerar os espaços\n Com Espaços {} \n Sem espaços {}'.format(len(name), len(name.replace(" ", ""))))
divisao = name.split()
print('Tamanho do primeiro nome\n tamanho {}'.format(len(divisao[0])))
