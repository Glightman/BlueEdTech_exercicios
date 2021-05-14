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