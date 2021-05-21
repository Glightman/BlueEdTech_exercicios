""" 2.	Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros
entre [1, 10] e cada valor associado é o número ao quadrado.
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}  """

numeros = {}
for num in range(0,10):
    numeros [num] = num**2
print(numeros)