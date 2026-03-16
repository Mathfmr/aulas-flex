#Você recebeu a lista de notas notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]. 
# Escreva um código que use um laço for para calcular a média de todas as notas. 
# Use uma list comprehension para criar uma nova lista chamada notas_aprovados contendo apenas as notas que são maiores 
# ou iguais a 7.0. Imprima a média e a lista de notas dos aprovados.
# notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]
# aprovados = [a for a in notas_brutas if a >=7]
# media = sum(notas_brutas) / len(notas_brutas)
# print(f'os aprovados são {aprovados}, e a média é {media}')




#Você recebeu a lista de registros de notas registros =
#  [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]. 
# Escreva um código que use um laço for com desempacotamento de tupla para calcular a média de todas as notas. 
# Imprima o nome do aluno com a maior nota.
# registros = [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]
# total = 0
# Maluno = ''
# Mnota = 0

# for n , i in registros:
#     total += i
#     if i >= Mnota:
#         Mnota = i
#         Maluno = n
# media = total / len(registros)

# print(f'{Maluno},{Mnota},{media:.2f}')

#Você tem uma lista de produtos e seus preços produtos = [('banana', 2.5), ('maçã', 4.0), ('laranja', 3.0)]. 
# Use uma dictionary comprehension para criar um dicionário a partir dessa lista de tuplas, 
# onde o nome do produto é a chave e o preço é o valor. Em seguida, use um laço for com o método .items() 
# para imprimir cada par chave-valor no formato: 'O preço da [chave] é R$ [valor]'.

# produtos = [('banana', 2.5), ('maçã', 4.0), ('laranja', 3.0)]
# transformar = {produto:valor for produto , valor in produtos}
# for p,v in transformar.items():
#     print(p,v)






#Crie um programa em Python que gerencie uma agenda de contatos utilizando dicionários e tuplas. 
# O programa deve: Permitir que o usuário adicione 3 contatos, onde cada contato tem nome (chave), 
# e-mail e telefone (armazenados em uma tupla).
#  Permitir que o usuário busque um contato pelo nome e exiba seus dados, se existir. 
# Exibir a agenda completa após a adição. 
# Passo a passo: 
# Criar um dicionário vazio agenda para armazenar os contatos. 
# Utilizar um laço for para permitir a adição de 3 contatos pelo usuário, pedindo nome, email e telefone. 
# Armazenar cada contato no dicionário, com a chave sendo o nome e o valor sendo uma tupla (email, telefone). 
# Pedir ao usuário o nome de um contato para buscar e exibir seus dados ou uma mensagem de “não encontrado”. 
# Exibir a agenda completa após todos os contatos adicionados, no formato: Nome: <nome> | E-mail: <email> | Telefone: <telefone>






