'''crie um programa que leia um nome de usuário e senha,
e se os mesmo estiverem corretos ele mostre uma mensagem de login efetuado com sucesso.
e se a pessoa não tiver um cadastro... ele mostre a opção de criar um.'''

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
        print('Seu cadastro foi criado com sucesso!')


