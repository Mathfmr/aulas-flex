#Você vai criar um programa que solicita ao usuário um número e informa se ele é positivo, negativo ou zero.
# Para isso: Utilize input() para ler o valor digitado pelo usuário. Converta o texto digitado para número 
# usando float(). Utilize uma estrutura condicional if/elif/else para determinar a situação do número: 
# Se o número for maior que 0, informe que é positivo. 
#Se o número for menor que 0, 
#informe que é negativo. Se o número for igual a 0, informe que o número é zero.

numero = float(input('informe seu numero '))

if numero == 0:
    print(f'o numero {numero} é 0neutro')
elif numero > 0:
    print(f'o numero {numero} é positivo')
else:
    print(f'o numero {numero} é negativo')

    