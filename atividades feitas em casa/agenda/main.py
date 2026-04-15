# main.py
# Script principal que usa os módulos tarefas e utilidades

import os
import tarefas
import utilidades


def exibir_menu():
    """Exibe o menu de opções."""
    print('\n========== AGENDA DE TAREFAS ==========')
    print('📅 Data atual: ' + utilidades.data())
    print('=' * 40)
    print('1  Adicionar tarefa')
    print('2  Listar tarefas')
    print('3  Remover tarefa')
    print('4  Concluir tarefa')
    print('5  Mostrar porcentagem concluída')
    print('6  Sortear uma tarefa aleatória')
    print('0  Sair')
    print('=' * 40)


def main():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            nome = input('Digite o nome da tarefa: ')
            descricao = input('Digite a descrição da tarefa: ')
            tarefas.adicionar_tarefa(nome, descricao)

        elif opcao == "2":
            tarefas.listar_tarefas()

        elif opcao == "3":
            tarefas.listar_tarefas()
            if len(tarefas.tarefas) > 0:
                try:
                    num = int(input('Digite o número da tarefa para remover: '))
                    tarefas.remover_tarefa(num - 1)
                except ValueError:
                    print('Digite um número válido!')

        elif opcao == "4":
            tarefas.listar_tarefas()
            if len(tarefas.tarefas) > 0:
                try:
                    num = int(input('Digite o número da tarefa para concluir: '))
                    tarefas.concluir_tarefa(num - 1)
                except ValueError:
                    print('Digite um número válido!')

        elif opcao == "5":
            utilidades.porcentagem(tarefas.tarefas)

        elif opcao == "6":
            utilidades.sorte(tarefas.tarefas)

        elif opcao == "0":
            print('Saindo da agenda... Até logo! 👋')
            break

        else:
            print('Opção inválida! Tente novamente.')


main()
