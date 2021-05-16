""" Desafio 2 - Faça um script que peça ao usuário o número de matérias da escola,
ou seja, um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de
cada matéria e isso será armazenado numa lista. Ao final, seu script deverá
fornecer a média geral do aluno. """

q = 0
lista = []
mat = int(input('Quantidade de matérias: '))
while q < mat:
    q += 1
    nota = float(input('Valor da {}º nota: '.format(q)))
    lista.append(nota)
soma = sum(lista)
div = soma/mat
print('-=-'*20)
print('Todas as notas das {} matérias foram: '.format(mat), lista)
print('-=-'*20)
print('A nota média é: {}'.format(div))
print('-=-'*20)


