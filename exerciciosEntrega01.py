#01 - Utilizando estruturas condicionais faça um programa
# que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, 
   # divida pelo resultado da divisão inteira e mostre o resultado na tela. 
   # Se não, mostre que a multiplicação não foi maior que 40.

def d():
   print('-=-'*20)
d()
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
d()
print('--> A soma desses números é igua a {}'.format(num1+num2))
print('--> A multiplicação entre esses números é igual a {}'.format(num1*num2))
d()
if num1>num2:
   print('--> O {} é o maior'.format(num1))
   print('--> A divisão inteira do primeiro número pelo segundo é igual a {}'.format(num1//num2))
   resultado = (num1*num2)/(num1//num2)
else:
   print('--> O {} é o maior'.format(num2))
   print('--> A divisão inteira do segundo número pelo primeiro é igual a {}'.format(num2//num1))
   resultado = (num1*num2)/(num2//num1)
if (num1+num2)%2==0:
   print('--> A soma entre os dois números é par')
else:
   print('A soma entre os dois números é ímpar')
if num1*num2>40:
   print('''--> O resultado da divisão entre 
   a multiplicação dos dois números e a divisão inteira dos mesmos é igual a {}'''.format(resultado))
else:
   print('--> A multiplicação entre os números não foi maior que 40')
d()


#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e 
# conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

print('RESPONDA APENAS COM "SIM" OU "NAO":')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
p1 = input('Telefonou para a vítima?  ').lower()
p2 = input('Esteve no local do crime?  ').lower()
p3 = input('Mora perto da vítima?  ').lower()
p4 = input('Devia para a vítima?  ').lower()
p5 = input('Já trabalhou com a vítima?  ').lower()
respostas = [p1,p2,p3,p4,p5]
contar = respostas.count('sim')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
if contar == 2:
    print('Você é um SUSPEITO!')
else:
    if contar == 3 or contar == 4:
        print('Você é um CÚMPLICE!')
    else:
        if contar == 5:
            print('Você é um ASSASSINO!')
        else:
            
            
            print('Você é INOCENTE!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e 
#cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

#08 - Crie um programa que leia nome, 
#ano de nascimento e carteira de trabalho e 
# cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

cadastro = dict()
nome = input('Seu nome: ')
ano = int(input('Seu ano de nascimento: '))
ctps = float(input('Numero da CTPS: '))
cadastro['nome'] = nome
cadastro['idade'] = 2021-ano
cadastro['ctps'] = ctps
if ctps != 0:
    ano2 = int(input('Ano de contratação: '))
    salário = float(input('Seu salário: '))
    cadastro['Ano de contratação'] = ano2
    cadastro['Salário'] = salário
    cadastro['Ano de aposentadoria'] = ano2 + 35
print(cadastro)