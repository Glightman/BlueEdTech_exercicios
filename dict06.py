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

pessoas = list() #ESTA VARIÁVEL É UMA LISTA QUE RECEBE POSTERIORMENTE TODOS OS DICIONARIOS CADASTRADOS.
idade1 = list() #ESTA VARIÁVEL É UMA LISTA QUE RECEBE TODAS AS IDADES PRA PODER SOMAR E FAZER UMA MÉDIA.
idadeAM = list() #ESTA ARIÁVEL É UMA LISTA PARA ARMAZENAR TODAS AS IDADES QUE ESTÃO ACIMA DA MÉDIA.
mulheres = list() #ESTA VARIÁVEL É UMA LISTA QUE SERVE PARA ARMAZENAR O NOME DE TODAS AS MULHERES.
fim = 1 #ESTA VARIÁVEL SERVE PARA VALIDAR O FUNCIONAMENTO DO WHILE.
quant_pess = 0 #ESTA VARIÁVEL É PARA CONTAR QUANTAS PESSOAS FORAM CADASTRADAS, -
#TODA VEZ QUE O WHILE RODAR ELE ADICIONA MAIS UM NESSA VARIÁVEL.
while fim == 1: #UM LOOP VALIDADO PELA VARIÁVEL 'FIM' A CIMA, QUANDO O VALOR DA VARIÁVEL MUDAR ELE PARA O LOOP.
    quant_pess += 1 #CONTADOR PRA AUMENTAR O VALOR DA VARIÁVEL quant_pess ACIMA.
    cadastro = dict() #ESTA VARIÁVEL ARMAZENA O DICIONÁRIO CRIADO NO LOOP.
    nome = input('Digite seu nome: ').upper() #INPUT PARA RECEBER O NOME DO USUÁRIO (.UPPER PARA COLOCAR EM LETRAS MAIÚSCULAS, OPCIONAL).
    # NESSE INPUT ABAIXO EU USO 3 ASPAS SIMPLES PARA POSSIBILITAR EU DAR 'PONTO PARÁGRAFO'.
    sexo = int(input('''Informe o seu gênero: 
    [ 1 ] para MASCULINO
    [ 2 ] para FEMININO
    --> : ''')) #INPUT PARA ARMAZENAR O SEXO.
    idade = int(input('Sua idade: ')) #INPUT PARA ARMAZENAR A IDADE.
    cadastro['nome'] = nome #NESSE MOMENTO É ADICIONADO O VALOR DA VARIÁVEL NOME AO DICIONÁRIO CADASTRO.
    idade1.append(idade) #NESTE MOMENTO O VALOR DA VARIÁVEL IDADE VAI SER ADICIONADA A UMA LISTA CHAMANDA IDADE1, -
    #PARA CALCULAR A MÉDIA DESSAS IDADES POSTERIORMENTE.
    if sexo == 1: #SE O SEXO FOR MASCULINO IRÁ ADICIONAR O VALOR DA VARIÁVEL SEXO NO DICIONÁRIO CADASTRO.
        cadastro['sexo'] = 'MASCULINO'
    else:
        if sexo == 2: #SE O SEXO FOR FEMININO IRÁ ADICIONAR O VALOR DA VARIÁVEL SEXO NO DICIONÁRIO CADASTRO.
            mulheres.append(nome)#E TAMBÉM IRÁ ADICIONAR O VALOR DA VARIÁVEL NOME À LISTA DE MULHERES.
            cadastro['sexo'] = 'FEMININO'
    pessoas.append(cadastro)#AO FINAL DO CADASTRO O .APPEND IRÁ ADICIONAR O DICIONÁRIO CADASTRO, RECÉM CRIADO, À LISTA PESSOAS.
    fim = int(input('''Deseja cadastrar outra pessoa?
    [ 1 ] SIM
    [ 0 ] NÂO
    --> : '''))# NESTE MOMENTO OCORRE A SAÍDA OU NÃO DO LOOPING DE CADASTRO DE PESSOAS SE DIGITAR 1 CONTINUA SE DIGITAR 0 ELE SAI DO LOOPING.
for a in idade1:#NESSA ESTRUTURA O FOR VAI VARRER A LISTA DE TODAS AS IDADES E FAZER UM CÁLCULO PARA SABER
#SE A EXISTE ALGUMA IDADE MAIO DO QUE A IDADE MÉDIA.
    if a > sum(idade1)/quant_pess:
        idadeAM.append(a) #SE EXISTIR, O .APPEND IRÁ ADICIONAR À LISTA DE 'IDADES ACIMA DA MÉDIA'.
def d():#AQUI ESTÁ UMA FUNÇÃO QUE EU CRIEI PARA FACILITAR A DECORAÇÃO DOS TEXTOS.
    print('-~-'*20)#TODA VEZ QUE EU CHAMAR ESSA FUNÇÃO (d()) O TERMINAL IRÁ PRINTAR UMA LINHA FEITA '-~-'.
d()
print('Foram cadastradas {} pessoas'.format(quant_pess))
d()
print('A média das idades é {:.0f}'.format(sum(idade1)/quant_pess))#AQUI EU USEI UM ':.0F' PARA NÃO TER NENHUMA CASA DECIMAL NA IDADE MÉDIA.
d()
print('''AS MULHERES SÃO: 
--> {}'''.format(mulheres))
d()
print('''AS IDADES QUE ESTÃO ACIMA DA MÉDIA SÃO: 
---> {}'''.format(idadeAM))
