#04 - Faça um programa que ajude um jogador da MEGA SENA
#  a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
#  e vai sortear 6 números entre 1 e 60 para cada jogo,
#  cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
quantNum = int(input('Quantos palpites você deseja criar?: '))
for p in range(0, quantNum):
    sleep(0.5)
    cont1 = 0
    palpite = []
    while cont1 < 6:
        cont1 += 1
        num = randint(1, 61)
        if num not in palpite:
            palpite.append(num)
        else:
            cont1 += 1
    print(palpite)
