#Programa de usuário e senha:

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
        print('~-~'*20)
        print('Seu cadastro foi criado com sucesso!')
        print('~-~'*20)
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
                print('~-~'*20)
                print('Seu cadastro foi criado com sucesso!')
                print('~-~'*20)
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
                print('~-~'*20)
                print('Você errou a senha 3 vezes')
                print('~-~'*20)
                fim += 1
            if key in passworld:
                print('~-~'*20)
                print('LOGIN EFETUADO COM SUCESSO! ')
