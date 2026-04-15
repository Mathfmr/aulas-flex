# utilidades.py
# Módulo responsável por funções auxiliares (datas, porcentagem concluída, sorteio)

import datetime
import math
import random


def data():
    data = datetime.datetime.now()
    return data.strftime('%d/%m/%Y %H:%M:%S')


def porcentagem(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
        return

    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    porcentagem = math.floor((concluidas / total) * 100)
    print(f'''Progresso: {concluidas}/{total} tarefas concluídas ({porcentagem}%)''')


def sorte(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada para sortear.')
        return

    tarefa = random.choice(tarefas)
    print(f'''🎲 Tarefa sorteada: '{tarefa['nome']}' - {tarefa['descricao']} [{"Concluída" if tarefa["concluida"] else "Pendente"}]''')
