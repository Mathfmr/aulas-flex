#Um supermercado quer controlar produtos e preços. 
# Crie uma lista de produtos: "arroz", "feijão", "macarrão". Crie uma tupla com os preços correspondentes: 
# 5.50, 7.20, 4.30. Pergunte ao usuário o nome de um produto e: Se estiver na lista, exiba o preço correspondente. 
# Se não estiver, informe que o produto não está disponível. Exiba todos os produtos com seus preços.
#primeiro fazer a lista com os produtos
#após isso fazer uma tupla com os  preços correspondentes
# terceiro perguntar o usuario o produto que ele deseja acessar o preço
#quarto condicional se tiver na lista mostrar o valor correspondente se não falar que não está disponivel
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
         





