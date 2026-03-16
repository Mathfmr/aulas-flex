# # Escreva uma função que simule um caixa eletrônico. 
# # A função saque deve receber o saldo atual da conta e o valor do saque. 
# # Ela deve verificar se o saldo é suficiente para o saque. 
# # Se for, deve imprimir 'Saque de R$ [valor] realizado com sucesso!' e o novo saldo. 
# # Se não for, deve imprimir 'Saldo insuficiente.' e o saldo atual. 
# # Chame a função para dois cenários: um com saque válido e outro com saque inválido.

# #def caixa(valor, saque):
# #         if saque < valor:
# #             print(f'Saque de R$ {saque} realizado com sucesso!')
# #             return(f'seu saldo atual é {valor - saque}')
# #         else:
# #             print('saldo insuficiente para saque')
        
# # valor = float(input('digite o saldo da sua conta: '))
# # saque = float(input('digite o valor que deseja sacar: '))
# # armazenar = caixa(valor,saque)

# # print(armazenar)
# # def numeros(*args):
# #     numeros1 = 0
# #     for i in args:
# #         numeros1 += i
# #     return numeros1

# # print(numeros(3,2,5,7))

# #Crie uma função chamada calcular_area que receba largura e altura como parâmetros e tenha um valor padrão de 1 para altura. Exiba a área.
# # def calcular_area(largura, altura= 1):
# #     area = largura * altura
# #     return area
# # print (calcular_area(9))


# Crie uma função cadastro que receba nome, idade e cidade usando **kwargs, e exiba cada dado.
# def cadastro(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'{chave}: {valor}')
# cadastro(nome = 'Matheus', idade= 23, cidade = 'BH')


# Crie uma função chamada media que recebe três números e retorna a média aritmética deles.
# def media(*args):
#     media_a = sum(args) / len(args)
#     return media_a
# print(media(5,7,4,2))


# Crie uma função desconto que recebe um preço e retorna o preço com 10% de desconto. A variável da taxa de desconto deve ser local à função.
def preço(valor):
    valor1 =  0.10
    return valor * (1 - valor1)

preço_com_desconto = preço(60)
print(preço_com_desconto)


