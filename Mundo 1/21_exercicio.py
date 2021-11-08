"Criar um algoritmo que toca um play de uma música"
import pygame
pygame.init()
pygame.mixer.music.load('Nome_do_aruivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()