"""Criar um programa que leia a velocidade de um carro com as sequintes condições
*Se ele ultrapassar 80km/h será multado com R$ 7,00 por km a mais acima do limite
*Caso esteja no limite não será multado"""

speed = float(input("Digite a velocidade do veículo:  "))
if speed >= 80:
    print('A multa por ultrapassar a velocidade será de \n'
          'R$ {:.2f} sendo R$ 7,00 por km a mais acima do limite'.format((speed - 80)*7))
else:
    print('O limite de velocidade não foi ultrapassado\n'
          'Sua velocidade foi de {:.2f} km/h'.format(speed))