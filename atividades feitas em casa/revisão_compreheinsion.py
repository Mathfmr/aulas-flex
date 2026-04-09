# Você tem uma lista de registros de notas: registros = [('Matemática', 8.5), ('História', 9.0), ('Matemática', 7.0)]. 
# Use um laço for para converter essa lista de tuplas em um dicionário, onde as chaves são as matérias e os valores são as notas.
#  Se houver notas duplicadas para a mesma matéria, a última nota deve ser a que prevalece. 
# Use um set comprehension para criar um set contendo todas as matérias únicas. 
# Imprima o dicionário final e o set de matérias únicas.
# registros = [('Matemática', 8.5), ('História', 9.0), ('Matemática', 7.0)]
# transformar = {registros: nota for registros, nota in registros}
# for m, n in transformar.items():
#     print (m,n)



# Crie uma lista de tarefas chamada lista_de_compras com os itens 'pão', 'leite', 'ovos'. 
# Use um laço for para imprimir cada item da lista. 
# Em seguida, adicione 'queijo' à lista e imprima o primeiro e o último item da lista atualizada.
# lista_de_compras = ['pão', 'leite', 'ovos']
# for i in lista_de_compras:
#     print(i)
# lista_de_compras.append('queijo')
# print(f'primeiro item da lista {lista_de_compras[0]}')
# print(f'ultimo item da lista {lista_de_compras[-1]}')





# Crie uma lista chamada registros que contenha as seguintes tuplas, representando o nome e o salário de funcionários: 
# [('Alice', 3000), ('Bob', 4500), ('Carol', 5000)]. 
# Use um laço for com desempacotamento de tuplas para imprimir cada registro no formato 'O salário de [Nome] é R$ [Salário]'.
# funcionários = [('Alice', 3000), ('Bob', 4500), ('Carol', 5000)]
# for n, s in funcionários:
#     print(f'O salário de {n} é R$ {s}')






# Crie um dicionário chamado contagem_votos a partir da lista de votos votos =
#  ['candidato A', 'candidato B', 'candidato A', 'candidato C']. 
# O dicionário deve mapear o nome de cada candidato para o número de votos que ele recebeu. Ao final, imprima o dicionário.


# votos = ['candidato A', 'candidato B', 'candidato A', 'candidato C']
# contagem_votos ={}  
# for voto in votos:
#     if voto in contagem_votos:
#         contagem_votos[voto] += 1
#     else:
#         contagem_votos[voto] = 1
# print("Contagem de votos:")
# print(contagem_votos)  


# Você tem um dicionário chamado alunos que mapeia o nome de cada aluno para a sua idade e cidade, por exemplo: 
# {'João': {'idade': 25, 'cidade': 'SP'}}. Crie um dicionário com pelo menos 3 alunos e seus dados (idade e cidade). 
# Escreva um código que percorra o dicionário e imprima uma frase para cada aluno no formato: 
# '[Nome do Aluno] tem [Idade] anos e mora em [Cidade].'
dados = {}
for i in range(3):
    nome = input(f'digite o nome do {i+1}º aluno: ')
    idade = int(input(f'digite a idade do {i+1}º aluno: '))
    cidade = input(f'digite a cidade do {i+1}º aluno: ')
    dados[nome] = (idade, cidade)
for n, d in dados.items():
    print(f'{n} tem {d[0]} anos e mora em {d[1]}.')

    