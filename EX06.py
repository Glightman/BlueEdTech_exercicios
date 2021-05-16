""" 6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
contratado para desenvolver o programa que monta a tabela de preços de pães,
de 1 até 50 pães, a partir do preço do pão informado pelo usuário """

import time as tm
valor = float(input('Preço do pão: '))
print('Panificadora Pão e Cia - tabela de preços ')
for p in range(1,51):
    cal1 = p*valor
    tm.sleep(0.1)
    print('{:2} - R$ {:.2f}'.format(p,cal1))