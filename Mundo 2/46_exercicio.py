"""Criar um programa que faça uma contagem repressiva de 10 até zero
Com intervalod e tempo de 1 segundo"""
#temporizador de tempo
import time
for i in range(10,-1,-1):
    time.sleep(1)
    print(i)