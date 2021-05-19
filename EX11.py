#01 - Crie um programa onde o usuário possa digitar sete valores numéricos e
#  cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

numTotal = list()
par = list()
impar = list()
for n in range(0,7):
   num = int(input('Digite um número '))
   numTotal.append(num)
   if num%2 == 0:
      par.append(num)
   else:
      if num%2 > 0:
         impar.append(num)
print('-=-'*20)
print('''Os números digitados foram: 
{}'''.format(numTotal))
print('-=-'*20)
print('''Os números ímpares desta lista são: 
{}'''.format(sorted(impar)))
print('-=-'*20)
print('''Os números pares dessa lista são: 
{}'''.format(sorted(par)))
print('-=-'*20)



#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.

