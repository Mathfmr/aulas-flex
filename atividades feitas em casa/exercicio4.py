#Crie um programa que peça ao usuário um número inteiro e determine: 
# Se o número é positivo, negativo ou zero. Se o número é par ou ímpar (apenas se for diferente de zero). 
# O programa deve exibir mensagens como: "Número positivo e par" "Número negativo e ímpar" "Número é zero"
numero = int(input('digite um numero '))
if numero == 0:
    print('numero neutro')
elif numero > 0:
    if numero % 2 == 0:
        print('positivo e par')
    else:
        print('positivo e impar')
else:
    if numero % 2 == 0:
        print('negativo e par')
    else:
        print('negativo e impar')

