"""Criar um programa que recebe um jogador e o número de gols e cria uma ficha
sobre esse jogador"""
def jogador(nome=False,gol=False):
    nome = str(input('Qual o nome do jogador:  '))
    gol = str(input('Quantos gols o jogador fez:  '))
    if nome and gol:
        print(f'Jogador {nome} fez {gol} gols')
    elif nome:
        print(f'O jogador {nome} fez 0 gols')
    elif gol:
        print(f'O jogador <desconhecido> fez {gol} gols')
    else:
        print('O jogador desconhedico fez 0 gols')

jogador()