#Crie um programa que cadastre alguns produtos e suas quantidades. 
# Primeiro, pergunte quantos produtos o usuário deseja cadastrar. 
# Em seguida, use um laço for para repetir o pedido do nome e da quantidade do produto o número de vezes informado. 
# Durante o laço, mostre na tela cada produto cadastrado no formato: Produto: X | Quantidade: Y
quantidade = int(input('quantos produtos deseja cadastrar: '))
for num in range(quantidade):
        x = input('qual o produto: ')
        y = int(input('qual a quantidade desse produto '))
        
        print(f'produto {x} | quantidade {y}')
