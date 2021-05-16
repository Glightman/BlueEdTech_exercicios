""" 5. Faça um programa que mostre os valores numéricos inteiros ímpares situados
na faixa de 0 a 20 """

import time as tm
for num in range(0,21):
    div = num%2
    if div > 0:
        tm.sleep(0.5)
        print(num)
print('\033[04;31mEsses são os numeros ímpares entre 0 e 20!...')
print('\033[0;37m_________________________________')