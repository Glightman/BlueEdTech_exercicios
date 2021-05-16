""" Desafio 1 - Escreva um programa que determine todos os números de 4
algarismos que possam ser separados em dois números de dois algarismos que
somados e elevando-se a soma ao quadrado obtenha-se o próprio número.
Exemplo: 3025 = 55 e 55**2 é igual á 3025 """

num = 0
for num in range(1000, 9999):
    div = num/100
    div2 = div%1
    conv = div2*100
    div3 = div//1
    som = conv+div3
    mult = som**2
    if num == mult:
        print(mult)