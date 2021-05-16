""" 3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e
mostre ao final a quantidade de pessoas de cada estado civil """

casado = 0
solteiro = 0
for pess in range(1, 16):
    ec = input('Qual o seu estado civil?  ')
    if ec == 'casado':
        casado += 1
    else:
        ec == 'solteiro'
        solteiro += 1
print('Temos {} solteiros e {} casados.'.format(solteiro, casado))