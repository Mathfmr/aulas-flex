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
contatos = {}
for i in range (3):
    nome = input(f'digite o seu nome: ')
    email = input('digte seu email: ')
    telefone = int(input('digite seu telefone: '))
    contatos[nome] = (email, telefone)

busca = input('digite um nome que esteja cadastrado: ')
if busca in contatos:
    for nomes, dados in contatos.items():
        print(f'Nome: {nomes} | Email:{dados [0]} | Telefone:{dados[1]} ')
else:
    print(' não encontrado')