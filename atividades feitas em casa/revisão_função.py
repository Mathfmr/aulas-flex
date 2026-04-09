# Crie um dicionário com 4 alunos e suas notas. Mostre apenas os alunos que tiraram nota maior ou igual a 7.
dados = {'matheus':10, 'marcio': 4, 'gabriel': 8, 'jessica' : 9}
for nome, nota in dados.items():
    if nota >=7:
        print(nome, nota)