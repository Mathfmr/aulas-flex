# tarefas.py
# Módulo responsável por manipular as tarefas (adicionar, listar, remover, concluir)

# Lista para armazenar as tarefas
tarefas = []


def adicionar_tarefa(nome, descricao):
    tarefa = {'nome': nome, 'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    print(f'''Tarefa '{nome}' adicionada com sucesso!''')


def listar_tarefas():
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
        return

    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f'''{i + 1}. {tarefa['nome']} - {tarefa['descricao']} [{status}]''')
    print()


def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        print(f'''Tarefa '{removida['nome']}' removida com sucesso!''')
    else:
        print('Índice inválido!')


def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        print(f'''Tarefa '{tarefas[indice]['nome']}' concluída!''')
    else:
        print('Índice inválido!')