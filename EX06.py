import time as tm
valor = float(input('Preço do pão: '))
print('Panificadora Pão e Cia - tabela de preços ')
for p in range(1,51):
    cal1 = p*valor
    tm.sleep(0.1)
    print('{:2} - R$ {:.2f}'.format(p,cal1))