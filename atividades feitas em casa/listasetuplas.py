# Projeto Final - Sistema de Cadastro de Alunos Objetivo Desenvolva um programa que cadastre 3 alunos, 
# colete suas notas e apresente um relatório final com a situação de cada um. Funcionalidades esperadas: 1.
#  Cadastro de dados Solicite o nome de 3 alunos Para cada aluno, peça sua nota (0 a 10) Armazene os dados em listas separadas 2. 
# Processamento Para cada nota, determine a situação: Nota ≥ 7: "Aprovado" Nota ≥ 5 e < 7: "Recuperação" Nota < 5: "Reprovado" 3. 
# Relatório final Exiba uma tabela organizada com: 
# Nome do aluno Nota obtida Situação acadêmica Exemplo de saída esperada: Nome Nota Situação ----------------------------- 
# Maria 9.0 Aprovado Renato 6.0 Recuperação Alan 3.0 Reprovado onceitos que você deve aplicar: 
# Listas para armazenar nomes e notas Loop for com range() para coletar dados Estruturas condicionais para classificar situações 
# Formatação de saída com espaçamento adequado
# notas = []
# nomes = []
# situação = []

# for i in range(3):
#     nomesA = input(f'digite o nome do aluno {i+1}: ')
#     notasA = float(input(f'digite a nota do aluno {i+1} de (0 a 10): '))
#     nomes.append(nomesA)
#     notas.append(notasA)
#     if notasA >=7:
#         situação.append('aprovado')
#     elif notasA >= 5:
#         situação.append('recuperação')
#     else:
#         situação.append('reprovado')
# for i in range(3):
#     print(f"{nomes[i]}, {notas[i]}, {situação[i]}")


#dicionario 

nn = {}
for i in range(3):
    nomesA = input(f'digite o nome do aluno {i+1}: ')
    notasA = float(input(f'digite a nota do aluno {i+1} de (0 a 10): '))
    
    if notasA >=7:
        situação = 'aprovado'
    elif notasA >=5:
        situação  ='recuperação'
    else:
        situação = 'reprovado'
    nn[nomesA] = (notasA , situação)
for n , d in nn.items():
    print(f"{n} {d[1]} {d[0]}")
    

    


