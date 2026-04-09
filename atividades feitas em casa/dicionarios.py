#Crie um programa em Python que cadastre alunos e suas notas em diferentes matérias. 
# O programa deve: 1. Permitir cadastrar o nome de um aluno. 2. 
# Associar um dicionário com matérias e notas desse aluno. 3. 
# Exibir todos os alunos cadastrados com suas notas. 
# Passo a passo da implementação: Criar um dicionário vazio alunos para armazenar os dados Criar um loop infinito (while True) 
# para cadastrar múltiplos alunos Solicitar o nome do aluno com input() e usar .strip() para remover espaços Verificar se o usuário 
# digitou "sair" para encerrar o programa Criar um dicionário vazio materias para as notas do aluno atual Criar outro loop infinito 
# para cadastrar múltiplas matérias Solicitar o nome da matéria e verificar se digitou "fim" para parar Solicitar a nota da 
# matéria e converter para float() Armazenar a matéria e nota no dicionário materias Associar o aluno e suas matérias no 
# dicionário principal alunos Exibir todos os alunos cadastrados usando loop for aninhado Iterar pelos alunos e suas 
# respectivas notas para mostrar os resultados Saida esperada: 
# --- Cadastro de Alunos --- Aluno: Mônica História: 9.0 Geografia: 7.0 Aluno: Lucas História: 5.0 Geografia: 8.0
#primero colocar o dicionario alunos
#segundo usar repetição while para infinitos cadastros de alunos
#terceiro se o usuario digitar sair o programa encerrar
#quarto cadastrar as materias e das mesmas se digitar fim para cadastrar outro aluno 
#cinco usar o for para ver o que ficou no dicionario alunos 
alunos = {}
while True:
    print('CADASTRO DE ALUNOS')
    alunoi = input('DIGITE O NOME DO ALUNO: ').strip()
    if alunoi == 'sair'.strip():
        print('programa de cadastro foi encerrado')
        break
    materias = {}
    while True:
        materiasI = input(f'DIGITE A MATERIA DO ALUNO {alunoi}: ')
        if materiasI == 'fim':
            print('cadastrar novo aluno')
            break
        notasa = float(input(f'QUAL A NOTA DA MATERIA {materiasI} '))
        materias[materiasI] = notasa
    alunos[alunoi] = materias
print('--- Cadastro dos alunos ---')
for a , m  in alunos.items():
    print(f'Aluno: {a}',)
    for mat , nota in m.items():
        print(f'{mat}: {nota}')
    
    



        
        
    