""" 3.	Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela. 
A média para aprovação é 7. 
Se o aluno tirar entre 5 e 6.9 está de recuperação, 
caso contrário é reprovado. """

school = {}
nome = input('Digite seu nome: ')
média = float(input('Sua nota: '))
school['nome'] = nome
school['média'] = média
if média >= 7:
    school['situação'] = 'Aprovado'
elif média < 7 and média >= 5:
    school['situação'] = 'Recuperação'
else:
    school['situação'] = 'Reprovado'
print(school)