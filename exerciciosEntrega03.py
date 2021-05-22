#03 - Utilizando estruturas de repetição com teste lógico, 
#faça um programa que peça uma senha para iniciar seu processamento, 
#só deixe o usuário continuar se a senha estiver correta, 
#após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
#onde o computador vai “pensar” em um número entre 0 e 10. 
#O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
#a cada palpite do usuário diga a ele se o número escolhido pelo computador 
#é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
def d():
   print('-=-'*20)
user = list()
passworld = list()
fim = 0
while fim == 0:
    option = int(input('''Escolha uma das opções abaixo:
    [ 1 ] Entrar
    [ 2 ] Cria conta
    [ 3 ] Finalizar
    -->:  '''))
    if option == 3:
        fim += 1
    elif option == 2:
        newUser = str(input('Crie um nome de usuário: '))
        while newUser in user:
            newUser = str(input('Este nome de usuário ja existe, tente outro: '))
        user.append(newUser)
        newPassworld = str(input('Crie uma senha: '))
        while len(newPassworld) < 6:
            newPassworld = str(input('A senha está muito curta, tente outra: '))
        passworld.append(newPassworld)
        d()
        print('Seu cadastro foi criado com sucesso!')
        d()
    elif option == 1:
        login = str(input('Nome de usuário: '))
        while login not in user:
            option2 = int(input('''Este nome de usuário não existe!
            Escolha uma opção:
            [ 1 ] Tentar novamente
            [ 2 ] Criar conta
            [ 3 ] Finalizar
            --> : '''))
            if option2 == 1:
                login = str(input('Nome de usuário: '))
            elif option2 == 2:
                newUser = str(input('Crie um nome de usuário: '))
                while newUser in user:
                    newUser = str(input('Este nome de usuário ja existe, tente outro: '))
                user.append(newUser)
                newPassworld = str(input('Crie uma senha: '))
                while len(newPassworld) < 6:
                    newPassworld = str(input('A senha está muito curta, tente outra: '))
                passworld.append(newPassworld)
                d()
                print('Seu cadastro foi criado com sucesso!')
                d()
            elif option2 == 3:
                fim += 1
        if login in user:
            key = str(input('Senha: '))
            cont = 0
            while key not in passworld and cont < 2:
                cont += 1
                key = str(input('''Senha incorreta!
                tente novamente: '''))
            if cont == 2:
                d()
                print('Você errou a senha 3 vezes')
                d()
                fim += 1
            elif key in passworld:
                d()
                print('LOGIN EFETUADO COM SUCESSO! ')
                fim += 1
sleep(2)
print('''SEJA BEM VINDO AO JOGO DA ADVINHAÇÃO!

LET`S GO!!!''')
sleep(3)
cont2 = 1
d()
print('A maquina está pensando em um número de 0 a 10...    ','AGUARDE...')
d()
sleep(5)
computador = randint(0,10)
print('Pronto!...')
sleep(2)
jogador = int(input('TENTE DESCOBRIR EM QUE NÚMERO EU PENSEI...: '))
while jogador != computador:
   if jogador > computador:
    print('....')
    sleep(2)
    print('HUMMM... Não foi dessa vez.')
    d()
    jogador = int(input('''Ta quase, eu pensei em um numero um pouco menor...
    Tente de novo
    --> : '''))
    cont2 += 1
   elif jogador < computador:
    print('....')
    sleep(2)
    print('HUMMM... Não foi dessa vez.')
    d()
    jogador = int(input('''Ta quase, eu pensei em um numero um pouco maior...
    Tente de novo
    --> : '''))
    cont2 += 1
if jogador == computador:
    d()
    print('PARABÉNS!!! VOCÊ ACERTOU!')
    print('A máquina pensou no número {}'.format(computador))
    d()
    sleep(0.7)
    print('Foram necessárias {} tentativas para acertar'.format(cont2))
    d()