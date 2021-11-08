"""Criar um programa que determine um valor aleatorio de 0 até 5
e que o usuário deva adivinhar qual é"""

import random
number_machine = random.randint(0,5)

number_user = int(input("Digite um número no intervalo de 0 até 5: "))
if number_machine == number_user:
    print('Você venceu, os números são iguais\n'
          'Máquina {}\n'
          'Usuário {}'.format(number_machine, number_user))
else:
    print('Você perdeu, os números são diferentes\n'
          'Máquina {}\n'
          'Usuário {}'.format(number_machine, number_user))