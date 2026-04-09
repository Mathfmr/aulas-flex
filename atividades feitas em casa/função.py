# Crie uma calculadora que execute as quatro operações matemáticas básicas 
# (soma, subtração, multiplicação e divisão) com dois números inteiros fornecidos pelo usuário. 
# O que seu programa deve fazer: Perguntar ao usuário qual operação ele deseja realizar Solicitar dois números inteiros 
# Executar a operação escolhida Exibir o resultado Requisitos obrigatórios: 
# Funções (4 funções obrigatórias): soma(numero1, numero2) - retorna a soma subtracao(numero1, numero2) - 
# retorna a subtração multiplicacao(numero1, numero2) - retorna a multiplicação divisao(numero1, numero2) - 
# retorna a divisão Entrada de dados: Capturar a operação desejada usando input() Capturar dois números inteiros usando input() e int() Lógica de controle:
#  Usar if/elif/else para identificar qual operação executar Usar .lower() para comparar a operação (ignorar maiúsculas/minúsculas) 
# Chamar a função correspondente Saída: Exibir o resultado formatado mostrando a operação e o valor calculado Exemplo de execução: 
# Digite o tipo de operação que deseja fazer: soma, subtração, multiplicação, divisão soma Digite o primeiro número: 10 Digite o segundo número: 
# 5 O resultado da soma foi 15
operação = input('Digite o tipo de operação que deseja fazer: soma, subtração, multiplicação, divisão:  ')
numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma

def subtração(numero1, numero2):
    subtração = numero1 - numero2
    return subtração

def multiplicação(numero1, numero2):
    multiplicação = numero1 * numero2
    return multiplicação

def divisão(numero1, numero2):
    divisão = numero1 / numero2
    return divisão

if operação == 'soma':
    print(soma(numero1, numero2))
elif operação == 'subtração':
    print(subtração(numero1, numero2))
elif operação == 'multiplicação':
    print(multiplicação(numero1, numero2))
elif operação == 'divisão':
    print(divisão(numero1, numero2))





