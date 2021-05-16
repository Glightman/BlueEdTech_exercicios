""" 1. Crie um código em Python que pede qual tabuada o usuário quer ver, em
seguida imprima essa tabuada """

num = int(input('DIGITE UM NÚMERO PARA VER SUA TABUADA:  '))
for cont in range(1,11):
    print('{} x {:2} = {}'.format(num, cont, num*cont))
    
   