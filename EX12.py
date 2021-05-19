#02 - Crie um programa que declare uma matriz de dimensão 3×3
#  e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com essa formatação:
""" 
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha]) 
 """

l1 = list()
l2 = list()
l3 = list()
matriz = [l1,l2,l3]
pares = list()
for n in range(0,9):
    num = int(input('Digite um número: '))
    if n >= 0 and n <= 2:
        l1.append(num)
    else:
        if n >= 3 and n <= 5:
            l2.append(num)
        else:
            n >= 6 and n <= 8
            l3.append(num)
    if num % 2 == 0:
        pares.append(num)
print(matriz[0])
print(matriz[1])
print(matriz[2])

#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
print(sum(pares))
   # B) A soma dos valores da terceira coluna.
print(l1[2]+l2[2]+l3[2]) 
   # C) O maior valor da segunda linha.
print(max(l2))