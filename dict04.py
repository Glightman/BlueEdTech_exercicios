""" 4.	Crie um programa em que 4 jogadores,
joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. 
No final coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado. 
Dicas: procure sobre a função randint(), 
sleep() e itemgetter da bliblioteca operator. """

from random import randint
from operator import itemgetter
dado = {}
for j in range(1,5):
    jog = randint(1,6)
    dado[f'jogador{j}'] = jog
dados = sorted(dado.items(), key=itemgetter(1), reverse=True)
print(dados)