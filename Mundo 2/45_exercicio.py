"""Criar um programa que jogue Jokenpô com o usuário"""


#módulo para randomizar as escolhas da máquina
import random

#Escolha do usuário
user = int(input('Escolha uma das opções abaixo para jogar\n'
           '0 - Pedra\n'
           '1 - Papel\n'
           '2 - Tesoura\n'))

#randomizando a escolha da máquina
list = ['Pedra','Papel','Tesoura']
user = list[user]
random.shuffle(list)
mach = list[0]

if user == mach:
    print('Deu empate\n'
          'O usuário escolheu {}\n'
          'E a máquina escolheu {}'.format(user, mach))
elif user == 'Pedra' and mach == 'Papel':
    print('A máquina venceu\n'
          'Escolha do jogador {}\n'
          'Escolha da máquina {}\n'.format(user, mach))
elif user == 'Pedra' and mach == 'Tesoura':
    print('A máquina perdeu\n'
          'Escolha do jogador {}\n'
          'Escolha da máquina {}\n'.format(user, mach))
elif user == 'Papel' and mach == 'Tesoura':
    print('A máquina venceu\n'
          'Escolha do jogador {}\n'
          'Escolha da máquina {}\n'.format(user, mach))
elif user == 'Tesoura' and mach == 'Pedra':
    print('A máquina venceu\n'
          'Escolha do jogador {}\n'
          'Escolha da máquina {}\n'.format(user, mach))
#ajustando os código