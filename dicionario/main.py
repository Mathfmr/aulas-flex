produtos = ['arroz', 'feijão', 'macarrão' ]
valores = (5.50 ,7.20 , 4.30)
print ('PRODUTOS DO SUPERMERCADO')
for i in range(3):
     print(f'Prdutos: {produtos[i]} valor: {valores[i]}')
while True:
    
    produto = input('Qual produto deseja (digite "sair" para encerrar o programa): ')
    if produto == 'arroz':
        print(f'o valor do {produto} é {valores[0]}')
    elif produto == 'feijão':
        print(f'o valor do {produto} é {valores[1]}')
    elif produto == 'macarrão':
        print(f'o valor do {produto} é {valores[2]}')
    elif produto == 'sair':
        print('PROGRAMA ENCERRADO')
        break
    else:
        print(f'o produto {produto} não está disponível')