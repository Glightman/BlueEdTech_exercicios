""" 6.	DESAFIO: Crie um programa que leia nome, 
sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, 
e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não. """

pessoas = list()
idade1 = list()
idadeAM = list()
mulheres = list()
fim = 0
quant_pess = 0
while fim == 0:
    quant_pess += 1
    cadastro = dict()
    nome = input('Digite seu nome: ').upper()
    sexo = int(input('''Informe o seu gênero:
    [ 1 ] para MASCULINO
    [ 2 ] para FEMININO
    --> : '''))
    idade = int(input('Sua idade: '))
    cadastro['nome'] = idade
    idade1.append(idade)
    if sexo == 1:
        cadastro['sexo'] = 'MASCULINO'
    else:
        if sexo == 2:
            mulheres.append(nome)
            cadastro['sexo'] = 'FEMININO'
    pessoas.append(cadastro)
    fim = int(input('''Deseja cadastrar outra pessoa?
    [ 0 ] SIM
    [ 1 ] NÂO
    --> : '''))
for a in idade1:
    if a > sum(idade1)/quant_pess:
        idadeAM.append(a)
def d():
    print('~-~'*20)
d()
print('Foram cadastradas {} pessoas'.format(quant_pess))
d()
print('A média das idades é {:.0f}'.format(sum(idade1)/quant_pess))
d()
print('''AS MULHERES SÃO: 
--> {}'''.format(mulheres))
d()
print('''AS IDADES QUE ESTÃO ACIMA DA MÉDIA SÃO: 
---> {}'''.format(idadeAM))
