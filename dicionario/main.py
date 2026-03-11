
# Crie um dicionário vendas que armazena o número de vendas por vendedor. 
# As chaves são os nomes e os valores são as vendas (ex: {"Ana": 10, "Bruno": 15, "Carla": 8}). 
# Adicione um novo vendedor, "Pedro", com 12 vendas. Depois, remova a vendedora "Carla" do dicionário. 
# Por fim, calcule e imprima a soma total de todas as vendas restantes.
# vendas = {'ana': 10, 'bruno': 15, 'carla':8}
# vendas['pedro'] = 12
# del vendas ['carla']
# soma = vendas.values()
# print(sum(soma))
# print(vendas)

#Você recebeu um dicionário que mapeia países e suas respectivas populações: 
# populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000} 
# Seu objetivo é descobrir qual país possui a maior população usando um loop for. 
# Passo a passo sugerido: Crie duas variáveis de controle: Uma para guardar o nome do país com maior população 
# (ex: pais_maior_pop), iniciando com uma string vazia. 
# Outra para guardar o valor da maior população encontrada até agora (ex: maior_pop), iniciando com 0. 
# Percorra o dicionário com um for, acessando o país e sua população. 
# A cada iteração, compare a população atual com o valor de maior_pop: Se a população atual for maior, 
# atualize as duas variáveis (maior_pop e pais_maior_pop). Ao final do laço, exiba na tela o resultado no formato: 
# O país com a maior população é: X com Y habitantes.
# populações = {'Brasil': 215_000_000, 'China': 1_100_000_000, 'EUA': 333_000_000, 'India': 1_220_000_000}
# paismaiorpop = ''
# maiorpop = 0
# for n, p in populações.values():
    
#     if p > maiorpop:
#         maiorpop = p
#         paismaiorpop = n
# print(maiorpop)
# print(paismaiorpop)
#Imagine que compradores_janeiro é um set com os clientes que compraram em janeiro compradores_janeiro = 
# {"João", "Maria", "Ana", "Carlos"} e compradores_fevereiro é um set com os clientes de fevereiro. 
# compradores_fevereiro = {"Ana", "Pedro", "João", "Juliana"} encontre os clientes que compraram apenas em janeiro. 
# Imprima o resultado.
compradores_jan = {'joão', 'Maria', 'Ana','Carlos'}
compradores_fev = {'Ana','pedro','joão','juliana'}
a = compradores_jan - compradores_fev
print(a)


